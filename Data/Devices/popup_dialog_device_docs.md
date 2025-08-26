# 📘 popup_dialog_device – UEFN Verse Device Documentation

## 🔹 Description
The `popup_dialog_device` allows you to display customizable HUD dialog popups to players during gameplay. These popups can include a title, description text, and interactive buttons. You can respond to button presses, detect timeouts, or handle dismissals with event listeners in Verse. This is ideal for tutorials, branching dialogue, confirmations, or mission choices.

---

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `popup_dialog_device`

---

## 🧩 Events (Data Members)
| Event Name              | Type                         | Description                                                   |
|------------------------|------------------------------|---------------------------------------------------------------|
| `ShownEvent`           | `listenable(agent)`          | Fires when the popup is shown to an agent.                    |
| `DismissedEvent`       | `listenable(agent)`          | Fires when the popup is dismissed (closed without selection). |
| `RespondingButtonEvent`| `listenable(tuple<agent, int>)` | Fires when a button is clicked, returns agent & button index.|
| `TimeOutEvent`         | `listenable(agent)`          | Fires when the popup times out (auto-dismissed).              |

---

## 🛠️ Functions & Methods

### 🎮 Display Control
| Function            | Description                                      |
|--------------------|--------------------------------------------------|
| `Show(agent)`      | Displays the popup to a specific player.         |
| `Show()`           | Displays the popup to all players.               |
| `Hide(agent)`      | Hides the popup from a specific player.          |
| `Hide()`           | Hides the popup from all players.                |
| `Enable()` / `Disable()` | Activates or deactivates the popup device.     |

### 🧾 Content & Text
| Function                        | Description                                           |
|--------------------------------|-------------------------------------------------------|
| `SetTitleText(text)`           | Sets the popup’s title. Max 32 characters.            |
| `SetDescriptionText(text)`     | Sets the main description. Max 350 characters.        |
| `SetButtonCount(count)`        | Sets number of buttons. Max 3. Call before `Show()`.  |
| `SetButtonText(index, text)`   | Sets label of specific button. Max 24 characters.     |
| `GetTitleText()` / `GetDescriptionText()` / `GetButtonText(index)` | Returns current title, description, or button label. |

### 📦 Transform & Positioning
| Function                  | Description                                                 |
|--------------------------|-------------------------------------------------------------|
| `GetTransform()`         | Returns position/rotation/scale (requires `IsValid()`).      |
| `MoveTo(position, rotation, duration)` | Smoothly moves the device.                      |
| `MoveTo(transform, duration)`           | Moves device using full transform.              |
| `TeleportTo(...)`        | Instantly moves the device.                                 |

---

## 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

popup_dialog_example := class(creative_device):

    @editable
    Popup : popup_dialog_device = popup_dialog_device{}

    OnBegin<override>()<suspends> : void =
        Popup.SetTitleText("Choose Your Path")
        Popup.SetDescriptionText("Do you want to enter the cave or stay outside?")
        Popup.SetButtonCount(2)
        Popup.SetButtonText(0, "Enter the Cave")
        Popup.SetButtonText(1, "Stay Outside")

        Popup.RespondingButtonEvent.Subscribe(OnButtonPressed)
        Popup.ShownEvent.Subscribe(OnShown)
        Popup.DismissedEvent.Subscribe(OnDismissed)
        Popup.TimeOutEvent.Subscribe(OnTimeout)

        # Show popup to first player who joins
        loop:
            Players := GetPlayspace().GetPlayers()
            if (Players.Length > 0):
                Popup.Show(Players[0])
                break
            Sleep(0.5)

    OnButtonPressed(Data : tuple<agent, int>) : void =
        let (Player, ButtonIndex) = Data
        if (ButtonIndex = 0):
            Print("Player chose to enter the cave.")
        else if (ButtonIndex = 1):
            Print("Player chose to stay outside.")

    OnShown(Player : agent) : void =
        Print("Popup shown to {Player}")

    OnDismissed(Player : agent) : void =
        Print("Popup dismissed by {Player}")

    OnTimeout(Player : agent) : void =
        Print("Popup timed out for {Player}")
```

---

## 🔧 How to Use in UEFN
1. **Place the Device**
    - Drag a `popup_dialog_device` into your level.
2. **Customize Content**
    - Set title, description, and number of buttons in Verse or in the Details panel.
3. **Connect to Verse Logic**
    - Handle player input using `RespondingButtonEvent`, `DismissedEvent`, and `TimeOutEvent`.
4. **Trigger the UI**
    - Use `Show(agent)` when ready (e.g., trigger zone, mission start).
5. **Build & Playtest**
    - Compile (`Ctrl+Shift+B`), test popup, verify interaction logic.

---

## 🧠 Best Practices
- Keep popups short (1–2 sentences) for clarity.
- Always call `SetButtonCount()` before `Show()`.
- Use player responses to control gameplay flow.
- Store choices for branching logic using Verse state.

---

## ❌ Common Issues & Solutions
| Issue                  | Problem                        | Solution                                      |
|------------------------|--------------------------------|-----------------------------------------------|
| Popup doesn’t show     | Device not enabled              | Use `Enable()` or call `Show(agent)` directly.|
| Buttons don't appear   | Button count not set first     | Use `SetButtonCount()` before `Show()`.       |
| Event doesn’t trigger | Missing `.Subscribe()`          | Ensure event handlers are properly subscribed.|
| Button text missing    | Empty string used              | Provide a short label (max 24 characters).    |

---

## 📎 Note
This device is **visual only** and does not apply gameplay effects directly. Pair it with Verse logic to implement choices that affect gameplay.

