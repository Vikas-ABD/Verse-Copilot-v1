📘 damage_volume_device – UEFN Verse Device Documentation

🔹 Description
The damage_volume_device creates a customizable volume (zone) on your Fortnite island that deals damage to agents (players/AI), vehicles, and creatures who enter or remain inside. This device supports instant elimination or damage-over-time, and is essential for hazards (like lava, death pits, traps), restricted areas, challenge arenas, or creative elimination logic.

🧱 Verse Using Statement
verse
using { /Fortnite.com/Devices }

🔗 Inheritance Hierarchy
* creative_object
* creative_device_base
* effect_volume_device
* damage_volume_device

🧩 Data Members (Events)
| Name              | Type              | Description                                |
|-------------------|-------------------|--------------------------------------------|
| AgentEntersEvent  | listenable(agent) | Fires when an agent enters the damage zone |
| AgentExitsEvent   | listenable(agent) | Fires when an agent exits the damage zone  |

🛠️ Functions & Methods
| Name                   | Description                                                                     |
|------------------------|---------------------------------------------------------------------------------|
| Enable()               | Activates the damage volume (starts applying damage/elimination).              |
| Disable()              | Deactivates the volume (no damage while disabled).                             |
| SetDamage(Damage: int)| Sets damage per tick (1–500); applies to "Damage Over Time" mode.             |
| GetDamage()            | Returns the current damage-per-tick value.                                     |
| UpdateSelectedClass(agent)| Changes the class mask; affected class is set to that of the agent passed. |
| UpdateSelectedTeam(agent)| Changes the team mask to match agent’s team.                               |
| GetAgentsInVolume()    | Gets all agents currently inside the volume.                                   |
| IsInVolume(agent)      | Checks if a specific agent is within the volume.                               |
| MoveTo()/TeleportTo()  | Move or teleport the device to another location.                               |
| GetTransform()         | Gets transform (world position/rotation/scale).                                |

🎛 Configuration Options (Details Panel)
* **Enabled on Phase:** When the device is enabled (Always, None, Pre-Game Only, Gameplay Only).
* **Zone Visible During Game:** Show/hide zone in game.
* **Base Visible During Game:** Show/hide base visual in game.
* **Zone Width/Depth/Height:** Set the size of the zone.
* **Damage Type:** Elimination or Damage Over Time (choose instant eliminate or ticking damage).
* **Damage:** Damage dealt per tick (1–500).
* **Damage Tick Rate:** How often damage is applied (if not instant elimination).
* **Affects Shields:** Whether damage affects shields before health.
* **Target Team/Class:** Restrict zone by team/class with inclusion/exclusion logic.
* **Affects Creatures/Guards/Players/Vehicles:** Fine control over affected types.
* **Zone Shape:** Box or Cylinder.

🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

damage_volume_example := class(creative_device):

    @editable
    DamageVolume : damage_volume_device = damage_volume_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    SetDamageButton : button_device = button_device{}

    @editable
    GetDamageButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        DamageVolume.AgentEntersEvent.Subscribe(OnAgentEnters)
        DamageVolume.AgentExitsEvent.Subscribe(OnAgentExits)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        SetDamageButton.InteractedWithEvent.Subscribe(OnSetDamagePressed)
        GetDamageButton.InteractedWithEvent.Subscribe(OnGetDamagePressed)

    OnAgentEnters(Agent : agent) : void =
        Print("Agent entered the damage volume!")

    OnAgentExits(Agent : agent) : void =
        Print("Agent exited the damage volume!")

    OnEnablePressed(Agent : agent) : void =
        DamageVolume.Enable()
        Print("Damage volume enabled!")

    OnDisablePressed(Agent : agent) : void =
        DamageVolume.Disable()
        Print("Damage volume disabled!")

    OnSetDamagePressed(Agent : agent) : void =
        DamageVolume.SetDamage(50)
        Print("Damage set to 50!")

    OnGetDamagePressed(Agent : agent) : void =
        Damage := DamageVolume.GetDamage()
        Print("Current damage is: {Damage}")
```

🛠 How It Works in UEFN:
1. **Place Devices in Level:**
   * Add a damage_volume_device at the hazard, pit, or zone where you want elimination/damage.
   * Optionally add multiple button_devices to enable, disable, or change settings at runtime.

2. **Configure Device in Details Panel:**
   * Set size, damage type, amount, tick rate, shield/health order, and affected teams/classes.
   * Configure phase and visibility options.

3. **Create & Build Verse Script:**
   * Add new Verse file (e.g., damage_volume_example.verse), paste code, and build (CTRL+SHIFT+B).

4. **Place and Reference Your Verse Device:**
   * Assign your placed devices to editable fields in the Verse class in the Details panel.

5. **Test and Refine:**
   * Launch a session, enter the zone to test damage, and use buttons to control behavior.

🧠 Best Practices
* Match volume size to in-game visuals.
* Use team/class filters to scope effect.
* Use Enable/Disable logic for dynamic gameplay.
* Keep damage values reasonable and fair.

❌ Incorrect Usage Examples and Fixes
| Issue | ❌ Wrong Example | ✅ Correct Example | Explanation |
|-------|------------------|--------------------|-------------|
| Invalid damage value | DamageVolume.SetDamage(9999) | DamageVolume.SetDamage(500) | Max value is 500 |
| Misuse of GetDamage | Print(DamageVolume.GetDamage) | Print(DamageVolume.GetDamage()) | Method requires parentheses |
| No filtering configured | None set | Set team/class in Details panel | Must define target filters |
| No event subscription | No .Subscribe used | DamageVolume.AgentEntersEvent.Subscribe(...) | Events must be subscribed |
| Devices unassigned | Not assigned in Details | Assign devices to Verse class | Devices must be linked |

🔖 Notes
* Use events for custom logic (eliminations, UI, traps).
* Dynamically update damage/team/class via Verse.
* Test across all agents/vehicles/creatures to verify logic.

