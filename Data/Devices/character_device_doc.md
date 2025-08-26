# character_device – UEFN Verse Device Documentation

## 🔹 Description
The `character_device` is an interactive, indestructible mannequin used within your Fortnite island. It allows for customizable character models with specific poses, outfits, and emotes. The mannequin can be made interactive to trigger Verse or device logic and is often used for:

- NPC-style displays
- Quest givers
- Poseable figures
- Social hubs
- Interactive narrative elements

It offers control over its appearance, idle animation or static pose, and emotes that can be triggered manually or by player interaction.

---

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `character_device`

---

## 🛠️ Key Features & Methods
| Method | Description |
|--------|-------------|
| `Enable()` | Enables the device, making it visible and/or interactable. |
| `Disable()` | Disables the device, hiding it or removing interactivity. |
| `Show()` | Makes the mannequin visible in the world. |
| `Hide()` | Hides the mannequin from the world. |
| `PlayEmote()` | Performs the selected emote. |
| `InteractedWithEvent` | Triggers when a player interacts with the device. |

---

## 🧹 Events (Data Members)
| Name | Type | Description |
|------|------|-------------|
| `InteractedWithEvent` | `listenable(agent)` | Fires when an agent interacts with this device. |

---

## 🎛 Device Options (Details Panel)
| Option | Description |
|--------|-------------|
| Character | Selects which Fortnite character/skin is displayed. |
| Use Animated Idle | If enabled, uses animated idle; otherwise, uses static pose. |
| Idle (Pose) / Idle (Animated) | Defines mannequin’s idle stance or animation. |
| Emote | Emote performed when triggered. |
| Interact Type | Can be None or Send Event Only. |
| Interaction Text/Time | Defines prompt text and hold time. |
| Visible During Game | Initial visibility state. Can be overridden in Verse. |
| Character Slot | For syncing with Character Device Controllers. |
| Enable Character Collision | Toggles mannequin's physical collision. |

---

## 🧰 Direct Binding / Channel Functions
You can use Verse or device wiring to:
- Show/Hide the mannequin
- Enable/Disable the device
- Trigger the mannequin to perform an emote

---

## 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

character_device_example := class(creative_device):

    @editable
    CharacterDevice : character_device = character_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    ShowButton : button_device = button_device{}

    @editable
    HideButton : button_device = button_device{}

    @editable
    EmoteButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        CharacterDevice.InteractedWithEvent.Subscribe(OnCharacterInteracted)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        ShowButton.InteractedWithEvent.Subscribe(OnShowPressed)
        HideButton.InteractedWithEvent.Subscribe(OnHidePressed)
        EmoteButton.InteractedWithEvent.Subscribe(OnEmotePressed)

    OnCharacterInteracted(Agent : agent) : void =
        Print("Character device interacted with by agent!")

    OnEnablePressed(Agent : agent) : void =
        CharacterDevice.Enable()
        Print("Character device enabled!")

    OnDisablePressed(Agent : agent) : void =
        CharacterDevice.Disable()
        Print("Character device disabled!")

    OnShowPressed(Agent : agent) : void =
        CharacterDevice.Show()
        Print("Character device shown!")

    OnHidePressed(Agent : agent) : void =
        CharacterDevice.Hide()
        Print("Character device hidden!")

    OnEmotePressed(Agent : agent) : void =
        CharacterDevice.PlayEmote()
        Print("Character device played emote!")
```

---

## 📚 How to Use in UEFN

### 1. Place Devices in Your Level
- Drag `character_device` and five `button_device` instances into the world.

### 2. Configure Device Options
- On `character_device`: set character, idle pose or animation, emote, interaction text, and other settings.
- On each button: position and label appropriately for their control function.

### 3. Create Your Verse Script
- Right-click in Verse Explorer → Create New Verse File (e.g., `character_device_example.verse`).
- Paste and save the example code.
- Build the script (Ctrl+Shift+B) until "Build Succeeded" appears.
- Drag the Verse device into the world.

### 4. Assign @editable References
- In the Verse device’s Details panel:
  - Set `CharacterDevice` to your `character_device` instance.
  - Assign the `EnableButton`, `DisableButton`, `ShowButton`, `HideButton`, and `EmoteButton` respectively.

### 5. Test In-Game
- Launch a play session.
- Press buttons to see the character respond: enable/disable, show/hide, emote.
- Interact with the mannequin to trigger `InteractedWithEvent`.

---

## 🧠 Best Practices
- Use `.PlayEmote()` to signal quest success, storytelling moments, or feedback.
- Combine `.Show()` / `.Hide()` with `.Enable()` / `.Disable()` for conditional logic.
- Sync multiple mannequins by assigning the same Character Slot and using a Character Device Controller.
- Subscribe to `InteractedWithEvent` for dialogue, item rewards, or scripted responses.

---

## ❌ Common Issues & Fixes
| Issue | Description | Solution |
|-------|-------------|----------|
| Device does not appear | Hidden or disabled initially | Use `.Show()` and `.Enable()` or update visibility in Details panel |
| Event not handled | Missing `.Subscribe()` call in Verse | Ensure event subscriptions are written as shown in example |
| Buttons do nothing | Unassigned @editable references | Set all device and button references in Details panel |
| Incorrect pose/emote | Misconfigured Details | Review pose, idle type, and emote settings in the Details panel |

---

## ⚠️ Note
- The `character_device` is indestructible and for visuals/interactivity only.
- Runtime and editor customization available for pose, emote, interaction, and logic.
- Designed to enhance storytelling, missions, and player immersion through visual triggers and interactivity.

