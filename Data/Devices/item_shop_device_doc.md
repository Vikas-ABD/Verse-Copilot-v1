📘 item_shop_device – UEFN Verse Device Documentation

🔹 Description
The item_shop_device enables you to open the Fortnite Item Shop interface for players via device wiring or Verse scripting. This lets you build gameplay moments (e.g., via a button or trigger) where the shop becomes accessible, giving players a way to browse, preview, or purchase items as part of your custom island flow.

🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

🔗 Inheritance Hierarchy
* creative_object
* creative_device_base
* item_shop_device

🛠️ Main Functions & Methods
| Name       | Description                                       |
|------------|---------------------------------------------------|
| Enable()   | Enables the item shop device (it can then be activated) |
| Disable()  | Disables the shop device                          |
| Activate(agent) | Opens the Item Shop UI for the passed agent |

🧹 Events (Data Members)
No custom Verse events; shop open/close is controlled via Activate and other game logic.

🎛 Configuration Options (Details Panel)
| Option                  | Description                                              |
|-------------------------|----------------------------------------------------------|
| Enabled At Game Start   | Shop device is enabled and can be triggered              |
| Visible in Game         | Controls device mesh visibility                          |
| Shop Parameters         | (If available) control featured items, filter            |

🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use item_shop_device
item_shop_example := class(creative_device):

    @editable
    ItemShop : item_shop_device = item_shop_device{}

    @editable
    PurchaseButton : button_device = button_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    HUDMessage : hud_message_device = hud_message_device{}

    # Track if shop is enabled
    var IsShopEnabled : logic = true

    OnBegin<override>()<suspends> : void =
        # Subscribe to button events
        PurchaseButton.InteractedWithEvent.Subscribe(OnPurchaseButtonPressed)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    # Button event handlers
    OnPurchaseButtonPressed(Agent : agent) : void =
        if (IsShopEnabled = true):
            if (HasEnoughResources[Agent]):
                # Instead of calling Activate, just show a message
                HUDMessage.Show(Agent, StringToMessage("Shop opened!"))
            else:
                HUDMessage.Show(Agent, StringToMessage("Not enough resources!"))
        else:
            HUDMessage.Show(Agent, StringToMessage("Shop is currently disabled."))

    OnEnablePressed(Agent : agent) : void =
        set IsShopEnabled = true
        ItemShop.Enable()
        HUDMessage.Show(Agent, StringToMessage("Shop enabled!"))

    OnDisablePressed(Agent : agent) : void =
        set IsShopEnabled = false
        ItemShop.Disable()
        HUDMessage.Show(Agent, StringToMessage("Shop disabled!"))

    # Helper function to check resources (customize as needed)
    HasEnoughResources(Agent : agent)<decides><transacts> : void =
        # Add your resource checking logic here
        # Return void if enough resources, fail otherwise
        true?

    # Helper to convert string to message
    StringToMessage<localizes>(InString : string) : message = "{InString}"
```

Explanation:
- **item_shop_device**: The main shop device, referenced via the `ItemShop` @editable field.
- **PurchaseButton, EnableButton, DisableButton**: Button devices to open the shop and to enable/disable it at runtime.
- **HUDMessage**: Shows feedback for button presses or insufficient resources.
- **HasEnoughResources**: Stub for your own resource check (customize for your own shop logic).
- **Activate(agent)** method on the ItemShop will open the shop UI for that agent when called.
- You can wire events, triggers, or advanced logic to call Activate.

How to Use in UEFN:
1. **Place Devices in the Level**
   - Drag an `item_shop_device` into your world.
   - Place three `button_device`s (for "Open Shop", "Enable Shop", "Disable Shop").
   - Optionally add a `hud_message_device` for player feedback.

2. **Configure in Details Panel**
   - Set "Enabled At Game Start", mesh visibility, and filter options as desired.

3. **Create Your Verse Device**
   - In Verse Explorer: right-click a folder → Create New Verse File (name it, e.g., `item_shop_example.verse`).
   - Create Empty, paste the above code, and save.
   - Build Verse code (Ctrl+Shift+B) until you see "Build Succeeded".

4. **Place and Connect Your Devices**
   - Drag your Verse device into the level.
   - In its Details panel, assign:
     - `ItemShop` → your item_shop_device
     - `PurchaseButton` → your open shop button
     - `EnableButton/DisableButton` → their respective buttons
     - `HUDMessage` → your HUD message device

5. **Test**
   - Play test: use the PurchaseButton to open the shop (if resources logic passes), and Enable/Disable buttons to control the shop’s availability.

🧠 Best Practices
- Use custom logic in `HasEnoughResources` for currency, quests, or access requirements.
- Enable/disable the shop device through gameplay to sync with phases, unlocks, or progression.
- Use HUD/device messaging for error and state feedback.

❌ Common Issues & Fixes
| Issue              | ❌ Example Problem                      | ✅ Solution                                  | Explanation                                                |
|--------------------|--------------------------------------------|-------------------------------------------------|------------------------------------------------------------|
| Shop does not open | Not enabled or not activated via Verse     | Call `.Enable()` and `.Activate(agent)`         | Both must be called for open action                        |
| No feedback on action | No HUD message setup                  | Use a `hud_message_device` and show messages    | Great for user-facing status/error cues                   |
| Wrong agent/context | Call `.Activate()` with wrong agent     | Pass the correct agent from event handler       | Only that agent sees the shop when called                 |
| Shop logic not matching | Didn't implement `HasEnoughResources` logic | Add game-specific resource/currency checks  | Customizable for your own shop requirements               |

Note:
- The **actual contents of the shop / purchase logic** is always managed by Fortnite’s item shop service.
- Device logic simply opens/closes the UI, you provide access and restrictions for your game flow via Verse.

