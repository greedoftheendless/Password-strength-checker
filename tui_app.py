from textual.app import App, ComposeResult
from textual.widgets import Input, Button, Static, Label
from analyzer import analyze_password
from wordlist_gen import generate_wordlist, save_wordlist

def get_strength_bar(score: int) -> str:
    bars = ["░░░░░", "█░░░░", "██░░░", "███░░", "█████"]
    emojis = ["💀", "⚠️", "🟡", "✅", "🔒"]
    labels = ["Very Weak", "Weak", "Fair", "Strong", "Very Strong"]
    return f"{bars[score]} {emojis[score]} {labels[score]}"

def get_custom_message(score: int) -> str:
    messages = [
        "This password is extremely weak. Avoid common patterns or dictionary words.",
        "Still guessable. Try adding symbols, numbers, and random words.",
        "Getting there! Add more complexity and length.",
        "Good. Could still improve with unique phrases or randomization.",
        "Excellent! This password is highly secure."
    ]
    return messages[score]

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

        yield Static("\n🚪 Exit")
        yield Button("Quit", id="quit")

    def on_button_pressed(self, event):
        if event.button.id == "analyze":
            password = self.password_input.value.strip()
            if password:
                score, suggestions = analyze_password(password)
                strength_bar = get_strength_bar(score)
                custom_msg = get_custom_message(score)
                suggest_text = "\nSuggestions: " + (", ".join(suggestions) if suggestions else "None")

                output = f"\n{strength_bar}\n{custom_msg}{suggest_text}"
                self.output_label.update(output)
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

        elif event.button.id == "quit":
            self.exit()

if __name__ == "__main__":
    app = PasswordToolApp()
    app.run()
