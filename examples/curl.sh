#!/usr/bin/env bash
# Placeholders only. Not run against the live service.
: "${WHATS360_USER:?}" "${WHATS360_PASSWORD:?}"
TOKEN=$(curl -s -X POST https://whats360.live/api/auth/login -H "Content-Type: application/json" \
  -d "{\"username\": \"$WHATS360_USER\", \"password\": \"$WHATS360_PASSWORD\"}" | python3 -c 'import sys,json; print(json.load(sys.stdin)["token"])')
curl -X POST https://whats360.live/api/v1/email/send \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d '{"from":"you@yourdomain.com","to":"recipient@example.com","subject":"Hello from API","body":"This is the email body."}'
