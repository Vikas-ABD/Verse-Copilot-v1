**UEFN Verse Device Documentation: conditional_button_device**

---

### 📙 Description
The `conditional_button_device` is a specialized button that players (agents) can only activate if they are carrying specific items in their inventory. This device is commonly used for puzzles, keycards, crafting mechanics, and multi-stage objectives where a player must possess or deliver set items to trigger actions in your Fortnite island.

You can configure:
- Item requirements
- Interaction text and timers
- Visual appearance
- Verse logic or event bindings for full gameplay control

---

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `conditional_button_device`

---

### 🧹 Data Members (Events)
| Name | Type | Description |
|------|------|-------------|
| ActivatedEvent | listenable(agent) | Signals when a player with all required items successfully activates the button. |
| NotEnoughItemsEvent | listenable(agent) | Signals when a player attempts to activate but is missing required items. |

---

### 🧰 Functions & Methods
| Name | Description |
|------|-------------|
| Activate(agent) | Activates the device as if triggered manually. |
| Enable() | Enables the button for interaction. |
| Disable() | Disables the button from interaction. |
| SetInteractionText(text) | Sets the interaction prompt (max 150 chars). |
| SetInteractionTime(time) | Sets interaction duration in seconds. |
| SetItemCountRequired(i, c) | Sets quantity for required item slot i (0-2). |
| GetInteractionTime() | Returns configured interaction time. |
| GetItemCount(agent) | Returns quantity of required items carried by the agent. |
| GetItemCountRequired(i) | Returns required quantity for slot i. |
| GetRemainingItemCountRequired(i) | Returns remaining quantity needed. |
| GetItemScore(i) | Returns score for a key item. |
| IsHoldingItem(agent) | Checks if agent holds any/all required items. |
| HasAllItems(agent) | Checks if agent has all required items. |
| Reset() | Resets device to its initial state. |
| Toggle(agent) | Toggles between enabled/disabled state. |
| TeleportTo() / MoveTo() | Moves device in the level (instant or animated). |

---

### 🎛 Configuration Options (Details Panel)
- **Number of Key Item Slots**: Up to 3 item types.
- **Key Items Required**: Quantity of each.
- **Allowed Team/Class**: Restricts usage.
- **Activate Team**: Further restricts activation.
- **Interact Time**: Duration required to activate.
- **Reset Delay**: Cooldown between activations.
- **Disable/Remain Unlocked**: Control post-activation state.
- **Show Key Item Hologram**: Displays required item model/icon.
- **Interaction/Missing Items Text**: Custom text feedback.
- **Appearance Options**: Icon, color, border settings.

---

### 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

conditional_button_example := class(creative_device):

    @editable
    ConditionalButton : conditional_button_device = conditional_button_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    SetTextButton : button_device = button_device{}

    @editable
    SetTimeButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        ConditionalButton.ActivatedEvent.Subscribe(OnActivated)
        ConditionalButton.NotEnoughItemsEvent.Subscribe(OnNotEnoughItems)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        SetTextButton.InteractedWithEvent.Subscribe(OnSetTextPressed)
        SetTimeButton.InteractedWithEvent.Subscribe(OnSetTimePressed)

    OnActivated(Agent : agent) : void =
        Print("Conditional button activated by agent!")

    OnNotEnoughItems(Agent : agent) : void =
        Print("Agent does not have required items!")

    OnEnablePressed(Agent : agent) : void =
        ConditionalButton.Enable()
        Print("Conditional button enabled!")

    OnDisablePressed(Agent : agent) : void =
        ConditionalButton.Disable()
        Print("Conditional button disabled!")

    OnSetTextPressed(Agent : agent) : void =
        ConditionalButton.SetInteractionText(StringToMessage("Press with Items"))
        Print("Conditional button interaction text set!")

    OnSetTimePressed(Agent : agent) : void =
        ConditionalButton.SetInteractionTime(2.0)
        Print("Conditional button interaction time set to 2.0 seconds!")

    StringToMessage<localizes>(InString : string) : message = "{InString}"
```

---

### 🔄 Step-by-Step Setup in UEFN
1. **Create the Verse Device**
   - Go to *Verse → Verse Explorer* in UEFN.
   - Right-click a folder, select *Create New Verse File* (e.g., `conditional_button_example.verse`).
   - Paste the above code and build (Ctrl+Shift+B).

2. **Place Devices in Your Level**
   - Drag your Verse device from Content Browser into the map.
   - Add a `conditional_button_device` and 4 `button_device` instances.

3. **Assign @editable References**
   - In Details panel:
     - Assign `ConditionalButton`, `EnableButton`, `DisableButton`, `SetTextButton`, `SetTimeButton`.

4. **Configure Conditional Button**
   - Set key item slots and drop items onto the button to register.
   - Adjust interaction time, text, team restrictions, etc.

5. **Test the Logic**
   - Start session, interact as a player with/without required items.
   - Watch log outputs and observe button behavior.

---

### 🧠 Best Practices
- Limit to 3 key item slots for clarity.
- Physically drop required items on the device to register them.
- Subscribe to both `ActivatedEvent` and `NotEnoughItemsEvent`.
- Combine with item granters, locks, or crafting systems for complex logic.

---

### ❌ Common Issues & Fixes
| Issue | ❌ Wrong Example | ✅ Correct Example | Explanation |
|-------|---------------------|------------------------|-------------|
| Items not assigned | Only set via Verse or UI | Drop items physically onto device | Needed to register them |
| No event subscription | Waiting for action | Use `.Subscribe()` | Required for logic to run |
| Too many items | 4+ items added | Max 3 key item slots | Device limit |
| Button doesn’t reset | No reactivation | Use `.Reset()` | Needed after activation |
| Blank references | Missing field assignment | Assign in Details panel | Mandatory for Verse to function |

---

**Note:** For more advanced systems (e.g., crafting or delivery), combine multiple conditional buttons and chain logic through Verse scripting to control progression and unlocks.

