# Reusable generic helpers that don't belong to any single page object

import re, time
from typing import Callable
from playwright.sync_api import Page, Locator, expect

class Helpers:

    @staticmethod
    def get_alert_text(page:Page)->str:
        alert = page.locator(".alert,[role='alert']").first
        expect(alert).to_be_visible(timeout=10_000)
        return (alert.text_content() or "").strip()

    @staticmethod
    def scroll_into_view(page:Page, selector:str)->None:
        page.locator(selector).first.scroll_into_view_if_needed()

    @staticmethod
    def retry_until(fn: Callable[[], bool], timeout_ms: int = 10_000, interval_ms: int = 500) -> bool:
        """Retries a callable until it returns True or the timeout elapses."""
        start = time.time()
        while (time.time() - start) * 1000 < timeout_ms:
            if fn():
                return True
            time.sleep(interval_ms / 1000)
        return False

    @staticmethod
    def auto_accept_dialogs(page:Page)->str:
        """Accepts any native browser dialog (used for OpenCart "remove item" confirms)."""
        page.on("dialog",lambda dialog: dialog.accept())