def wait_for_bios_update(self, timeout=300):
    """Wait until BIOS information is sent to Icicle (max timeout seconds)."""
    start = time.time()
    while time.time() - start < timeout:
        self.menu.open_menu_item("Host")
        if not self.info.IsGetCachedInfoWarningDisplayed():
            bios_version = self.info.GetBiosVersionValue()
            if bios_version and bios_version != "":
                return True
        time.sleep(5)
    return False
