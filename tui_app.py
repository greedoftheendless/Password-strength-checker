from textual.app import App, ComposeResult
from textual.widgets import Input, Button, Static, Label
from analyzer import analyze_password
from wordlist_gen import generate_wordlist, save_wordlist

class PasswordToolApp(App):
    def compose(self) -> ComposeResult:
        yield Static("🔐 Password Strength Analyzer")
        self.password_input = Input(placeholder="Enter password to analyze")
        yield self.password_input
        yield Button("Analyze Password", id="analyze")
        self.output_label = Label("")
        yield self.output_label

        yield Static("\n🧰 Wordlist Generator")
        self.inputs_input = Input(placeholder="Enter name pet dob etc...")
        yield self.inputs_input
        yield Button("Generate Wordlist", id="generate")

    def on_button_pressed(self, event):
        if event.button.id == "analyze":
            password = self.password_input.value.strip()
            if password:
                score, suggestions = analyze_password(password)
                out = f"Score: {score}/4\nSuggestions: {', '.join(suggestions) if suggestions else 'None'}"
                self.output_label.update(out)
            else:
                self.output_label.update("⚠️ Please enter a password.")

        elif event.button.id == "generate":
            raw_input = self.inputs_input.value.strip()
            if raw_input:
                user_inputs = raw_input.split()
                wordlist = generate_wordlist(user_inputs)
                save_wordlist(wordlist)
                self.output_label.update(f"✅ Saved {len(wordlist)} words to wordlist.txt")
            else:
                self.output_label.update("⚠️ Please enter some inputs.")

if __name__ == "__main__":
    app = PasswordToolApp()
    app.run()
