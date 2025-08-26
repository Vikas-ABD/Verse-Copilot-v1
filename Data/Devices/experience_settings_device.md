📘 experience_settings_device – UEFN Verse Device Documentation

🔹 Description
The experience_settings_device is used to set and customize high-level properties for your game mode in Unreal Editor for Fortnite (UEFN). This device centralizes key rule and environment overrides, allowing you to tailor the core rules of your island experience—such as advanced game rules, win/loss conditions, scoring mechanics, environmental parameters, and other global settings. Use this device to ensure consistency and to override basic My Island/game settings for advanced islands or game modes.

🧱 Verse Using Statement
verse
using { /Fortnite.com/Devices }

🔗 Inheritance Hierarchy
* creative_object
* creative_device_base
* experience_settings_device

🧩 Configuration Options (Details Panel)
| Option                    | Description |
|--------------------------|-------------|
| Game Mode                | Choose or override the base game mode (Free For All, Teams, Custom). |
| Round/Match Rules        | Duration, win/lose conditions, sudden elimination, etc. |
| Time of Day/Lighting     | Override skybox/time settings, force fixed time of day. |
| Score & Victory Rules    | Set win condition (eliminations, score, objectives) and tie-break. |
| Player Limits            | Min/max player count, enable mid-game join/leave. |
| Matchmaking Options      | Queueing region, ratings, pairing logic (if supported). |
| Environmental Settings   | Gravity, movement, audio/atmospheric overrides. |
| Behavior Flags           | Universal mechanics flags (building, item pickup, respawn rules, etc). |
| Post-Game/Restart Behavior | Adjust return to lobby, restart, or round sequence. |

*(Configure all game-wide settings from this device in its Details panel. Some settings may override similar My Island/game rules.)*

🛠️ Functions & Methods
| Name     | Description |
|----------|-------------|
| Enable() | Ensures the device is active and applying its settings. |
| Disable()| Disables the device (useful for debugging/dev swaps). |

(No major Verse-settable functions as of v35.20; config is UI-driven)

🪩 Events
Currently, no runtime events are exposed in Verse for this device; configuration is generally set before play in UEFN.

🛠️ Verse Usage Example
You typically reference this device in Verse to ensure it’s enabled and to clarify initialization steps, but its primary configuration is always in the Details panel. Here’s a simple Verse template for reference and readiness checks:

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use experience_settings_device
experience_settings_example := class(creative_device):

    @editable
    ExperienceSettings : experience_settings_device = experience_settings_device{}

    OnBegin<override>()<suspends> : void =
        # No event subscription needed - just demonstrate usage
        Print("Experience settings device initialized")
```

Explanation:
* The script exposes one experience_settings_device as an @editable field.
* Upon game start (OnBegin), you can confirm activation or perform related logic.
* No special event subscriptions or runtime code control is necessary for most scenarios—configuration is handled via the Details panel.

Step-by-Step Setup in UEFN
1. **Place the Device in Your Level**
   * Find and drag an experience_settings_device into your world.

2. **Configure Experience Settings**
   * In the Details panel, specify your desired game mode, timing, player limits, scoring, round/win/loss conditions, environmental flags, and other properties.

3. **(Optional) Add a Verse Script for Device Reference**
   * In Verse Explorer: right-click a folder and *Create New Verse File* (e.g., experience_settings_example.verse).
   * Use the example script above to reference the device and confirm readiness or hook into complex setups.
   * Click *Verse → Build Verse Code* (Ctrl+Shift+B) until “Build Succeeded”.
   * Drag your Verse device into the level and, in its Details, assign:
     * ExperienceSettings → your placed experience_settings_device

4. **Test Your Game Mode**
   * Play-test to verify all configured high-level rules are in effect.

🧠 Best Practices
* Use exactly one experience_settings_device for streamlined global rules—avoid conflicting duplicate configurations.
* For advanced experiences, pair with other global/round devices (round_settings_device, etc.)—configure the interaction order as needed.
* Verify all settings override defaults as intended—check them in Details rather than Verse code.

❌ Common Issues & Fixes
| Issue                          | ❌ What Not to Do                            | ✅ Do This                                 | Why? |
|-------------------------------|------------------------------------------------|--------------------------------------------|------|
| Editing only My Island settings | Changed settings in “My Island” only         | Always set in the device for full override | Device settings take precedence |
| Multiple devices conflicting   | Placed several experience_settings_devices    | Use only one device for consistency        | Prevents conflicts/override wars |
| Not enabling device            | Device left disabled in Details               | Set “Enabled” or call .Enable() in Verse if needed | Device must be active |
| Attempting to configure runtime in Verse | Tried to change all settings via Verse | All core configs are set in the Details panel | Device is not Verse-dynamic |

Note:
* Use this device when you want reliable, global control of high-level game rules and environment for your island.
* Level-wide changes take precedence over My Island/game defaults when this device is enabled and configured.

