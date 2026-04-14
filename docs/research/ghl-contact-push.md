# GHL Contact Push Integration

**Verified:** 2026-03-22  
**API Version:** 2021-07-28  
**Location ID:** ZS5wuDbXMdtD5ua94ZPo

---

## Endpoints

| Action | Method | URL |
|--------|--------|-----|
| Create contact | POST | `https://services.leadconnectorhq.com/contacts/` |
| Update contact | PUT  | `https://services.leadconnectorhq.com/contacts/{id}` |
| List custom fields | GET | `https://services.leadconnectorhq.com/locations/{locationId}/customFields` |
| Create custom field | POST | `https://services.leadconnectorhq.com/locations/{locationId}/customFields` |

## Required Headers

```
Authorization: Bearer {GHL_API_KEY}
Version: 2021-07-28
Content-Type: application/json
```

---

## Create Contact Payload

```json
{
  "locationId": "ZS5wuDbXMdtD5ua94ZPo",
  "firstName": "...",
  "lastName": "...",
  "email": "...",
  "phone": "...",
  "source": "LexCapital Bot",
  "tags": ["Bot Qualified Lead", "{deal_type}"]
}
```

Note: Create the contact first, then update with custom fields in a second PUT call.
Custom fields are ignored on initial POST — must be set via PUT.

---

## Custom Field Update Payload

Use field `id` (not `fieldKey`) and `field_value`:

```json
{
  "customFields": [
    {"id": "FIELD_ID", "field_value": "value"}
  ]
}
```

---

## Field IDs (verified live)

| Field | fieldKey | ID |
|-------|----------|----|
| Loan Type | contact.loan_type | Idsqfp89FqvlRSsUdCp0 |
| Loan Amount | contact.loan_amount | aNNVCBMclPY6mkJ7M9gC |
| Property Address | contact.property_address | np3XynHz8YSyMprTOyou |
| Property State | contact.property_state | hnOSQnZMxd5kD4yAfAdT |
| Exit Strategy | contact.exit_strategy | Ds63hTfnRS3W6CLuttnY |
| Verdict Score | contact.verdict_score | Yo7BbdlYHSXNC9qBSl1f |
| Matched Lender Count | contact.matched_lender_count | rK2nOT2wSsyCTl3NPg8z |
| Deal Status | contact.deal_status | gJWZTdnkmmfGva0Q8YSK |
| Referral Source | contact.referral_source | d3XBxu4KOUdJxhtYd8gA |

Parent group ID for all deal fields: `oBChmY18PANWrWxvIPCG`

---

## Integration Pattern (LexCapital Bot → GHL)

```
Step 1: POST /contacts/         → creates contact, returns contact.id
Step 2: PUT  /contacts/{id}     → sets all 9 custom fields using field IDs above
Step 3: GHL triggers 7-day follow-up sequence based on tag = deal_type
```

---

## Notes

- `customFields` array in the POST response is always empty — this is expected
- Always include `locationId` in the POST body
- Tags are lowercased automatically by GHL
- SSH to VPS (206.189.71.176) was refusing connections on 2026-03-22 — n8n webhook URL unknown, skipped in test
