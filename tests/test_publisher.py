import pytest
from datetime import datetime
from config import TZ, CATEGORIES
from scripts.publish_quiz import run_publisher, determine_auto_slot, get_due_categories_today

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

def test_get_due_categories_today():
    # Test at 07:05 IST
    dt_morning = datetime(2026, 11, 22, 7, 5, tzinfo=TZ)
    due_morning = get_due_categories_today(dt_morning)
    assert due_morning == ["Telangana History"]

    # Test at 12:15 IST (slots 0-5 due: 7, 8, 9, 10, 11, 12)
    dt_noon = datetime(2026, 11, 22, 12, 15, tzinfo=TZ)
    due_noon = get_due_categories_today(dt_noon)
    assert len(due_noon) == 6
    assert due_noon[0] == "Telangana History"
    assert due_noon[-1] == "Indian Geography"

    # Test at 20:30 IST (all 14 due)
    dt_night = datetime(2026, 11, 22, 20, 30, tzinfo=TZ)
    due_night = get_due_categories_today(dt_night)
    assert len(due_night) == 14
    assert due_night == CATEGORIES

