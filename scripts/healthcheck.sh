#!/bin/bash
LOGFILE="/home/lexbot/healthcheck.log"
BOT_TOKEN="8392331786:AAHRBoVumOqF98bvORRvQCz9j3vxDnTLqM8"
USER_ID="1233729131"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

send_telegram() {
    curl -s -X POST "https://api.telegram.org/bot${BOT_TOKEN}/sendMessage" \
        -d chat_id="${USER_ID}" \
        -d text="$1" > /dev/null 2>&1
}

if systemctl is-active --quiet openclaw; then
    echo "$TIMESTAMP [OK] openclaw is running" >> "$LOGFILE"
    exit 0
fi

echo "$TIMESTAMP [WARN] openclaw not running, attempting restart" >> "$LOGFILE"
systemctl restart openclaw >> "$LOGFILE" 2>&1
sleep 5

if systemctl is-active --quiet openclaw; then
    echo "$TIMESTAMP [RECOVERED] openclaw restarted successfully" >> "$LOGFILE"
    send_telegram "[LEX Bot] Auto-restarted successfully at ${TIMESTAMP}"
else
    echo "$TIMESTAMP [FAILED] openclaw failed to restart" >> "$LOGFILE"
    send_telegram "[LEX Bot] ALERT: Failed to restart at ${TIMESTAMP}"
fi
