import os
import requests

ACCESS_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN")
ORG_ID = os.environ.get("LINKEDIN_ORG_ID", "").strip()
ISSUE_BODY = os.environ.get("ISSUE_BODY", "")
ISSUE_NUMBER = os.environ.get("ISSUE_NUMBER")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REPO = os.environ.get("REPO")

# --- DIAGNOSTIC MONITOR ---
print("--- PRE-FLIGHT CHECK ---")
print(f"Raw ORG_ID from GitHub Vault: '{ORG_ID}'")
print(f"Target Author URN: urn:li:organization:{ORG_ID}")
print("------------------------")
# --------------------------

try:
    clean_text = ISSUE_BODY.split("---")[1].strip()
except IndexError:
    clean_text = ISSUE_BODY.strip()

url = "https://api.linkedin.com/v2/ugcPosts"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "X-Restli-Protocol-Version": "2.0.0",
    "Content-Type": "application/json"
}

post_data = {
    "author": f"urn:li:organization:{ORG_ID}",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {"text": clean_text},
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
}

response = requests.post(url, headers=headers, json=post_data)

if response.status_code == 201:
    print("Successfully posted to LinkedIn!")
    
    issue_url = f"https://api.github.com/repos/{REPO}/issues/{ISSUE_NUMBER}"
    issue_headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    requests.patch(issue_url, headers=issue_headers, json={"state": "closed"})
    requests.post(f"{issue_url}/comments", headers=issue_headers, json={"body": "✅ Successfully published to QuantumBeads LinkedIn page."})
else:
    print(f"Failed to post. Status code: {response.status_code}")
    print(response.text)
    exit(1)