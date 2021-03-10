class States:
    def __init__(self, view, main):
        self.view = view
        self.main = main

    def reset_start_button(self, start_button, stop_button, browser_btn):
        start_button.setEnabled(True)
        stop_button.setDisabled(True)
        browser_btn.setEnabled(True)