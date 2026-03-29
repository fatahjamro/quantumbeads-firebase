import os
import requests

ACCESS_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN")
ORG_ID = os.environ.get("LINKEDIN_ORG_ID", "").strip()
ISSUE_BODY = os.environ.get("ISSUE_BODY", "")
ISSUE_NUMBER = os.environ.get("ISSUE_NUMBER")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REPO = os.environ.get("REPO")
# 1. Extract the pure text from the GitHub Issue
try:
    parts = ISSUE_BODY.split("---")
    if len(parts) >= 3:
        # Rejoin everything between our top and bottom GitHub issue dividers
        raw_draft = "---".join(parts[1:-1]).strip()
    else:
        raw_draft = ISSUE_BODY.strip()
        
    # 2. Sever the sources from the final post
    if "---SOURCES---" in raw_draft:
        clean_text = raw_draft.split("---SOURCES---")[0].strip()
    else:
        clean_text = raw_draft
        
    # Strip out any conversational introductory text Gemini might add
    clean_text = clean_text.replace("Here's a highly technical yet accessible LinkedIn post for C-suite executives on a recent quantum computing advancement:", "").strip()
    
except Exception:
    clean_text = ISSUE_BODY.strip()

print("--- PRE-FLIGHT CHECK ---")
print(f"Targeting Company Page URN: urn:li:organization:{ORG_ID}")
print("------------------------")

# 2. Use the Modern LinkedIn REST Endpoint
url = "https://api.linkedin.com/rest/posts"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "LinkedIn-Version": "202602", 
    "X-Restli-Protocol-Version": "2.0.0",
    "Content-Type": "application/json"
}

post_data = {
    "author": f"urn:li:organization:{ORG_ID}",
    "commentary": clean_text,
    "visibility": "PUBLIC",
    "distribution": {
        "feedDistribution": "MAIN_FEED",
        "targetEntities": [],
        "thirdPartyDistributionChannels": []
    },
    "lifecycleState": "PUBLISHED",
    "isReshareDisabledByAuthor": False
}

response = requests.post(url, headers=headers, json=post_data)

if response.status_code == 201:
    print("✅ Successfully posted to the QuantumBeads Company Page!")
    
    # 3. Clean up the GitHub Issue
    issue_url = f"https://api.github.com/repos/{REPO}/issues/{ISSUE_NUMBER}"
    issue_headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    requests.patch(issue_url, headers=issue_headers, json={"state": "closed"})
    requests.post(f"{issue_url}/comments", headers=issue_headers, json={"body": "✅ Successfully published to the QuantumBeads Company LinkedIn feed."})
else:
    print(f"Failed to post. Status code: {response.status_code}")
    print(response.text)
    exit(1)