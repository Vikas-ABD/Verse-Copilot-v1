# 📘 campfire_device – UEFN Verse Device Documentation

## 🔹 Description
The `campfire_device` allows you to add a functional campfire to your Fortnite island using UEFN. This device creates a healing zone: when agents (players, AI, etc.) enter the effect area and the campfire is lit, they receive health regeneration through periodic pulses. Players can interact with the campfire to light or extinguish it, and optionally add wood if fuel is enabled. All actions can be automated or controlled via Verse code.

## 🛡 Imports Required
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
```

## 🔗 Inheritance Hierarchy
- `creative_object` - *Base class for creative devices and props.*
- `creative_device_base` - *Base class for creative_device.*
- `campfire_device`

## 🧹 Core Events & Methods
| Name | Type/Signature | Description |
|------|----------------|-------------|
| `AgentEntersEffectAreaEvent` | `listenable(agent)` | Fires when an agent enters the healing zone. |
| `AgentExitsEffectAreaEvent` | `listenable(agent)` | Fires when an agent exits the healing zone. |
| `AgentPulsedEvent` | `listenable(agent)` | Fires for each pulse that heals an agent inside the area while the campfire is lit. |
| `CampfirePulseEvent` | `listenable(tuple())` | Fires each time the campfire sends its healing pulse. |
| `LitEvent` | `listenable(agent)` | Fires when a player or agent lights the campfire. |
| `ExtinguishedEvent` | `listenable(agent)` | Fires when a player or agent extinguishes the campfire. |
| `EnabledEvent` | `listenable(tuple())` | Fires when the device is enabled. |
| `DisabledEvent` | `listenable(tuple())` | Fires when the device is disabled. |
| `Enable()` | `void` | Enables the device (can now interact/use). |
| `Disable()` | `void` | Disables the device (cannot interact or heal anymore). |
| `AddWood()` | `void` | Adds wood (if fuel is enabled, keeps fire burning longer). |
| `Light(agent)` | `void` | Lights the campfire (can be called from Verse or by player interaction). |
| `Extinguish(agent)` | `void` | Extinguishes the campfire. |

## 📃 Configuration Options (Details Panel)
- **Start Lit**: Yes / No – Campfire is burning at start.
- **Can Be Lit/Extinguished**: Yes / No – Allow players to light/extinguish.
- **Time to Light/Extinguish**: Set seconds required for these actions.
- **Uses Wood**: Yes / No – If Yes, wood must be added to keep it burning.
- **Health Per Pulse**: Amount of HP given each pulse.
- **Pulse Interval**: Time between healing pulses.
- **Campfire Zone Size**: Area in meters for healing effect.
- **Affected Team**: Heal specific team, all, or none.

## 🛠 Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

campfire_example := class(creative_device):

    @editable
    Campfire : campfire_device = campfire_device{}
    @editable
    EnableButton : button_device = button_device{}
    @editable
    DisableButton : button_device = button_device{}
    @editable
    LightButton : button_device = button_device{}
    @editable
    ExtinguishButton : button_device = button_device{}
    @editable
    AddWoodButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        EnableButton.InteractedWithEvent.Subscribe(OnEnableCampfire)
        DisableButton.InteractedWithEvent.Subscribe(OnDisableCampfire)
        LightButton.InteractedWithEvent.Subscribe(OnLightCampfire)
        ExtinguishButton.InteractedWithEvent.Subscribe(OnExtinguishCampfire)
        AddWoodButton.InteractedWithEvent.Subscribe(OnAddWood)

    OnEnableCampfire(Agent : agent) : void =
        Campfire.Enable()
        Print("Campfire enabled")

    OnDisableCampfire(Agent : agent) : void =
        Campfire.Disable()
        Print("Campfire disabled")

    OnLightCampfire(Agent : agent) : void =
        Campfire.Light(Agent)
        Print("Campfire lit")

    OnExtinguishCampfire(Agent : agent) : void =
        Campfire.Extinguish(Agent)
        Print("Campfire extinguished")

    OnAddWood(Agent : agent) : void =
        Campfire.AddWood()
        Print("Wood added to campfire")
```

## 🧠 Best Practices
- Configure all properties (healing rate, zone size, wood usage, etc.) in the **Details Panel** before runtime.
- Use `Enable()` and `Disable()` for game phase control, puzzles, or scripted gameplay.
- Leverage events (`LitEvent`, `ExtinguishedEvent`, `AgentPulsedEvent`, etc.) to add effects, achievements, or progress in quests.
- If using wood as fuel, ensure there are wood-adding mechanics or collectibles in your game to support continuous burning.

## ❌ Incorrect Usage Examples and Fixes
| Issue | ❌ Wrong | ✅ Correct | Explanation |
|-------|-----------|--------------|-------------|
| Not assigning device ref | Methods without `@editable` assignment | Assign campfire device in Details panel | Prevents nil or undefined reference errors |
| Skipping Enable() | Using campfire functions after `Disable()` | Call `Enable()` before `Light()` or `AddWood()` | Disabled devices cannot be used until re-enabled |
| Missing Agent param | `Campfire.Light()` or `Campfire.Extinguish()` | Always use `Campfire.Light(agent)` | These methods require an agent argument |

## 💡 Notes
- This device supports a wide range of gameplay types: survival, adventure, puzzle, RPG, and more.
- Events provide real-time interaction triggers for custom behavior and logic.
- Always pass the agent involved in any interaction to track specific player actions or status.
- Combine this device with other devices (buttons, achievements, collectibles) for rich game mechanics.

