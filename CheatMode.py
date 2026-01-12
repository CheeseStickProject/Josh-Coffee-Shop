
import tkinter as tk


def enable_cheat_mode(root, callback=None, show_button=False):
    """Enable a simple cheat binding on the provided Tk root.

    - Binds <Control-v> to trigger the cheat action.
    - If callback is provided it will be called when cheat is activated.
    - If show_button=True a small "Cheat" button will be packed in the root.

    The default action (when callback is None) prints "Hello World" to the
    terminal which is handy for quick testing.
    """

    def _default_action():
        print("Hello World")

    def _on_event(event=None):
        if callback:
            try:
                callback()
            except Exception as e:
                # avoid crashing the UI if the callback misbehaves
                print(f"Cheat callback error: {e}")
        else:
            _default_action()

    # Bind Ctrl+V to the cheat action
    root.bind('<Control-v>', lambda ev: _on_event(ev))

    # Optionally expose a small button to trigger the same action
    if show_button:
        btn = tk.Button(root, text="Cheat", command=lambda: _on_event())
        btn.pack(anchor="ne", padx=4, pady=4)
        return btn

    return None


if __name__ == "__main__":
    # quick manual test: run this file directly to open a tiny window
    test_root = tk.Tk()
    test_root.title("CheatMode Test")
    enable_cheat_mode(test_root, show_button=True)
    test_root.mainloop()
