import pytest
from scripts.publish_quiz import run_publisher

@pytest.mark.asyncio
async def test_publisher_dry_run():
    # Dry run should succeed and return exit code 0
    exit_code = await run_publisher(count=2, dry_run=True)
    assert exit_code == 0

