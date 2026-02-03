# audit_logger.py
import hashlib
from datetimeimport datetime

LOG_FILE ="policy_audit.log"

deflog_decision(ip, prompt, decision, reason, rule):
    prompt_hash = hashlib.sha256(prompt.encode()).hexdigest()

withopen(LOG_FILE,"a")as f:
        f.write(
f"{datetime.utcnow()} | IP={ip} | "
f"DECISION={decision} | REASON={reason} | "
f"RULE={rule} | PROMPT_HASH={prompt_hash}\n"
        )
