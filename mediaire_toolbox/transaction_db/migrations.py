"""SQL Commands that need to be issued in order to migrate the TransactionsDB
from one version to another. Keyed by target version ID."""
MIGRATIONS = {
    2: [
        "ALTER TABLE transactions ADD COLUMN task_progress INT DEFAULT 0",
        "UPDATE transactions SET task_progress = 10 WHERE processing_state = 'spm_lesion'",
        "UPDATE transactions SET task_progress = 10 WHERE processing_state = 'spm_volumetry'",
        "UPDATE transactions SET task_progress = 80 WHERE processing_state = 'volumetry_assessment'",
        "UPDATE transactions SET task_progress = 90 WHERE processing_state = 'report'",
        "UPDATE transactions SET task_progress = 100 WHERE processing_state = 'send_to_pacs'"    
    ],
    3: [
        "ALTER TABLE transactions ADD COLUMN task_skipped INT DEFAULT 0",
    ],
    4: [
        "ALTER TABLE transactions ADD COLUMN task_cancelled INT DEFAULT 0",
    ],
    5: [
        "ALTER TABLE transactions ADD COLUMN status TEXT",
        "ALTER TABLE transactions ADD COLUMN institution TEXT",
        "ALTER TABLE transactions ADD COLUMN sequences TEXT",
        "UPDATE transactions SET status = 'sent_to_pacs' WHERE processing_state = 'send_to_pacs'",
        "UPDATE transactions SET status = 'unseen' WHERE processing_state != 'send_to_pacs'"
        # institution & sequences to be filled out by 2.0.0 programmatic migration
    ]
}
