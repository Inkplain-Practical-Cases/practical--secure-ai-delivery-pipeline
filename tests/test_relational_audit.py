"""Test release HTTP audit SQLite foreign keys."""
import sqlite3
from app.providers.provider_record_request_audit import provider_record_request_audit
def test_release_api_audit(tmp_path):
    db=str(tmp_path/"release.sqlite3")
    rid=provider_record_request_audit("POST","/release",200,9.1,db)
    with sqlite3.connect(db) as conn:
        assert conn.execute("SELECT COUNT(*) FROM release_api_requests WHERE id=?",(rid,)).fetchone()[0]==1
        assert conn.execute("SELECT COUNT(*) FROM release_api_events WHERE request_id=?",(rid,)).fetchone()[0]==1
        assert conn.execute("PRAGMA foreign_key_check").fetchall()==[]
