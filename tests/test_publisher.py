import pytest
from scripts.publish_quiz import run_publisher, determine_auto_slot

@pytest.mark.asyncio
async def test_publisher_dry_run():
    # Dry run should succeed and return exit code 0
    exit_code = await run_publisher(count=2, delay_between_posts=0, dry_run=True)
    assert exit_code == 0

@pytest.mark.asyncio
async def test_publisher_daily_14_dry_run():
    # Full 14-subject daily rotation dry run
    exit_code = await run_publisher(daily_14=True, delay_between_posts=0, dry_run=True)
    assert exit_code == 0

@pytest.mark.asyncio
async def test_publisher_slot_dry_run():
    # Slot-based dry run for slot 3 (Indian Polity)
    exit_code = await run_publisher(slot_index=3, delay_between_posts=0, dry_run=True)
    assert exit_code == 0

def test_determine_auto_slot():
    slot = determine_auto_slot()
    assert 0 <= slot <= 13

