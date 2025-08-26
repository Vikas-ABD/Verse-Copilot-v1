📘 **disguise_device – UEFN Verse Device Documentation**

---

### 🔹 Description
The `disguise_device` allows you to apply cosmetic disguises to players, giving them the appearance of a different character model or role. Disguises can be applied automatically on spawn or manually through Verse or gameplay triggers. They can also be removed or broken based on custom conditions (e.g., taking damage, attacking, or entering a restricted zone).

**Perfect for:**
- Stealth missions or infiltration gameplay
- Roleplay mechanics (e.g. guards, civilians)
- Deception-based PvP modes
- Objective or narrative disguises (e.g. wear a disguise to gain access)

---

### 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
| Class                  | Description                                                   |
|------------------------|---------------------------------------------------------------|
| `creative_object`      | Base for all props/devices.                                   |
| `creative_device_base` | Adds device behavior (enable/disable, transform).             |
| `disguise_device`      | Allows players to wear and lose disguises based on logic.     |

---

### 🔌 Exposed Interfaces
| Interface   | Description                                            |
|-------------|--------------------------------------------------------|
| `enableable`| Enables/disables device via logic or gameplay triggers|

---

### 🔁 Listenable Events
| Event Name                      | Type                     | Description                                                                 |
|--------------------------------|--------------------------|-----------------------------------------------------------------------------|
| `ApplyDisguiseEvent`           | listenable(agent)        | Fired when a disguise is successfully applied to a player.                 |
| `BreakDisguiseEvent`           | listenable(agent, ?agent)| Fired when a disguise is broken (e.g., from damage). Optional second agent.|
| `RemoveDisguiseEvent`          | listenable(agent)        | Fired when disguise is removed via `RemoveDisguise()` not broken.         |
| `ShouldApplyDisguiseOnPlayerSpawn` | ?logic               | If true, applies disguise to players on spawn (must pass filter).          |

---

### 🧰 Core Methods
| Method Signature                         | Description                                                                           |
|------------------------------------------|---------------------------------------------------------------------------------------|
| `Enable(): void`                         | Enables the device so it can apply disguises.                                        |
| `Disable(): void`                        | Disables the device (existing disguises persist).                                    |
| `ApplyDisguise(Player: agent): void`     | Applies disguise to a player if allowed.                                             |
| `RemoveDisguise(Player: agent): void`    | Removes disguise applied by this device from the player.                            |
| `IsDisguiseApplied(Player: agent): logic`| Returns true if this device currently disguises the given player.                  |
| `IsEnabled(): logic`                     | Returns whether the device is currently enabled.                                     |
| `GetTransform()`, `MoveTo()`, `TeleportTo()` | Standard transform control for the device (not typically used in disguise logic). |

---

### ⚙️ Configuration Options (Details Panel)
| Option                | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `Disguise Asset`      | The disguise mesh/model to apply (selectable in UEFN).                      |
| `Apply on Spawn`      | Automatically apply disguise when the player spawns.                        |
| `Stomp Existing Disguise` | Whether this device overrides other active disguises.                 |
| `Break on Damage`     | Disguise breaks when the player takes damage.                               |
| `Break on Attack`     | Disguise breaks if the player uses a weapon or deals damage.               |
| `Filter by Team/Class`| Limit which players can receive the disguise.                              |

---

### 🚦 Example Usage in Verse
```verse
using { /Fortnite.com/Devices }

disguise_handler := class(
    @editable DisguiseDevice: disguise_device
)

OnBegin<override>()<suspends>: void =
    DisguiseDevice.Enable()
    DisguiseDevice.ApplyDisguiseEvent.Subscribe(OnDisguiseApplied)
    DisguiseDevice.BreakDisguiseEvent.Subscribe(OnDisguiseBroken)

ApplyTo(Player: agent): void =
    DisguiseDevice.ApplyDisguise(Player)

RemoveFrom(Player: agent): void =
    DisguiseDevice.RemoveDisguise(Player)

OnDisguiseApplied(Player: agent): void =
    Print("🕵️ Disguise applied to: {Player}")

OnDisguiseBroken(Player: agent, Breaker?: agent): void =
    Print("⚠️ Disguise broken on: {Player}")
```

---

### 🧠 Best Practices
- Use for stealth gameplay where players must blend in to bypass guards or areas.
- Combine with:
  - `trigger_device` to apply disguise when entering an area
  - `hud_message_device` to give player disguise status updates
  - `elimination_feed_device` to notify other players of disguise breaks
- Enable `Apply on Spawn` for persistent disguise roles (e.g., impostors or undercover players).
- Carefully configure disguise break conditions (attack, damage, proximity) for balance.
- If using multiple disguise devices, set `Stomp Existing Disguise = true` only when one disguise should override another.

---

### ❌ Common Mistakes & Fixes
| Issue                       | ❌ Wrong                                   | ✅ Fix                                                            |
|----------------------------|--------------------------------------------|------------------------------------------------------------------|
| Disguise not applying      | Forgot `Enable()` or invalid team/class    | Call `Enable()` and check device filter options                   |
| Disguise removed unexpectedly| Another device stomped it               | Set `Stomp Existing Disguise = false` in the other device         |
| Disguise doesn’t break on combat | Settings misconfigured              | Check if `Break on Damage`/`Attack` is enabled                    |

---

### ✅ Great for:
- Stealth and spy gameplay
- Role-based PvP deception (e.g., impostor mechanics)
- Infiltration missions with disguise-based puzzles
- Changing identity during match phases or cutscenes
- Tutorial disguises for class-based training

