# Earth Sprite Device – UEFN Verse Device Documentation

## 📙 Description
The `earth_sprite_device` creates a friendly interactive sprite, similar to the Earth Sprites in Fortnite Battle Royale. Players can trade their weapons to this sprite in exchange for either a random legendary weapon or a reward from a custom loot list.

This device supports:
- Trade logic
- Trade limits (per-player or global)
- Persistent tracking
- Runtime customization via Verse
- Enable/Disable control

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `earth_sprite_device`

## 🛠️ Key Functions & Methods
| Method | Description |
|--------|-------------|
| `Enable()` | Enables the device and resets all trade counts. |
| `Disable()` | Disables the device, preventing all interaction. |
| `EnableItemGranting()` | Enables item granting (trades return reward items). |
| `DisableItemGranting()` | Disables item granting (trade consumes input, gives no reward). |
| `EnableTradingForPlayer(agent)` | Enables trading for the specified player and resets their trade count. |
| `DisableTradingForPlayer(agent)` | Disables trading for the specified player. |
| `Show()` | Makes the Earth Sprite visible. |
| `Hide()` | Hides the Earth Sprite from view and interaction. |
| `IsEnabled()` | Returns `true` if enabled, `false` otherwise. |
| `GetTransform()` | Returns the sprite's world transform. |
| `MoveTo()` / `TeleportTo()` | Moves or teleports the sprite in the world. |

## 🧹 Events (Data Members)
| Name | Type | Fires When... |
|------|------|----------------|
| `WeaponConsumedEvent` | `listenable(agent)` | Player gave the sprite a weapon to trade. |
| `GrantTimerCompletedEvent` | `listenable(?agent)` | Sprite finished grant timer and rewarded the player. |

## 🎛 Device Configuration (Details Panel)
| Option | Description |
|--------|-------------|
| Enabled at Game Start | Whether sprite can be used at match start. |
| Grant Timer | Duration before reward is granted after trade. |
| Usable by Team/Class | Specify which teams/classes can interact. |
| Visible During Game | Whether sprite is visible during gameplay. |
| Item Granting | If off, trades consume input but give no rewards. |
| Trade Limit | Number of trades allowed before disabling (per-player or global). |
| Add To Global Count | Share trade limits among all sprites (Yes = global, No = per-player). |
| Override Label/Welcome/Success/Deny Text | Custom in-game interaction prompts. |

## 🪠 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

earth_sprite_example := class(creative_device):

    @editable
    EarthSprite : earth_sprite_device = earth_sprite_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    TradeButton : button_device = button_device{}

    @editable
    HUDMessage : hud_message_device = hud_message_device{}

    OnBegin<override>()<suspends> : void =
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        TradeButton.InteractedWithEvent.Subscribe(OnTradePressed)

    OnEnablePressed(Agent : agent) : void =
        EarthSprite.Enable()
        HUDMessage.Show(Agent, StringToMessage("Earth Sprite enabled!"))

    OnDisablePressed(Agent : agent) : void =
        EarthSprite.Disable()
        HUDMessage.Show(Agent, StringToMessage("Earth Sprite disabled!"))

    OnTradePressed(Agent : agent) : void =
        HUDMessage.Show(Agent, StringToMessage("Trade initiated!"))

    StringToMessage<localizes>(InString : string) : message = "{InString}"
```

### Explanation:
- **EarthSprite**: Reference to placed `earth_sprite_device`.
- **Buttons**: Used to control enable/disable/trade.
- **HUDMessage**: Optional visual feedback to players.
- **Events**: Hook into `WeaponConsumedEvent` or `GrantTimerCompletedEvent` for added effects.

## 📆 How to Use in UEFN
### 1. Place Devices in Your Level
- Add an `earth_sprite_device` to your level.
- Optionally add control buttons and HUD devices.

### 2. Configure Sprite in Details Panel
- Set **Grant Timer**, **Trade Limits**, **Loot Logic**, **Team Access**, **Custom Messages**, and **Visibility**.

### 3. Create Verse Script
- In Verse Explorer: Right-click folder > `Create New Verse File`.
- Paste the example script.
- `Build` (Ctrl+Shift+B) until "Build Succeeded."

### 4. Assign @editable References
- In your placed Verse device, assign the Earth Sprite and buttons in the Details panel.

### 5. Test
- Launch session to verify trading works as expected.

## 🧠 Best Practices
- Use `WeaponConsumedEvent` for achievements and bonuses.
- Call `EnableTradingForPlayer()` to reset trade count.
- Use `Show()` and `Hide()` to gate or reveal interaction phases.
- Customize loot and prompts for unique gameplay.

## ❌ Common Issues & Fixes
| Issue | Problem | Solution | Explanation |
|-------|---------|----------|-------------|
| No reward | "Item Granting" off | Turn on "Item Granting" | Must be enabled to give loot |
| Trades blocked | Trade Limit hit | Adjust limit or call `Enable()` | Limits can be global or per-player |
| Invisible sprite | Not shown/enabled | Use `.Enable()` + `.Show()` | Both required for interactivity |
| No feedback | No HUD message | Add HUD or Verse message logic | UI is fully customizable |

## 📌 Notes
- Only **weapons** can be traded.
- Rewards are either **random legendary** or **custom loot**.
- Core functionality is built-in; use Verse for customization, logic flow, and UI/UX enhancements.

