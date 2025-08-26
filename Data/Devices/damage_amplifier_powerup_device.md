📘 damage_amplifier_powerup_device – UEFN Verse Device Documentation

🔹 Description
The damage_amplifier_powerup_device is used to temporarily amplify an agent’s damage output. When a player picks up this powerup, all weapons they use deal multiplied damage for a configurable duration. You can set the damage multiplier, effect duration, respawn properties, visibility, team/class access, and more. This device is ideal for powerup pickup gameplay, boss encounters, or competitive balancing.

🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

🔗 Inheritance Hierarchy
* creative_object
* creative_device_base
* powerup_device
* damage_amplifier_powerup_device

🧩 Data Members (Events)
| Name | Type | Description |
|------|------|-------------|
| ItemPickedUpEvent | listenable(agent) | Signals when an agent picks up the powerup. |

🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| SetMagnitude(float) | Sets the powerup’s damage multiplier (e.g., 2.0 for double damage). |
| GetMagnitude() | Returns the current magnitude multiplier. |
| SetDuration(float) | Sets how long (in seconds) the powerup effect lasts after pickup. |
| GetDuration() | Gets the set effect duration. |
| Spawn() | Spawns the powerup into the world for player(s) to collect. |
| Despawn() | Removes the powerup from the world. |
| Pickup(agent) | Instantly applies the effect to an agent (direct pickup). |
| GetRemainingTime(agent) | Checks how much time an agent has left on the effect; returns 0 if none. |
| HasEffect(agent) | Checks if an agent currently has the amplifier effect. |
| Enable() / Disable() | Allows or prevents all interaction with the device. |
| Show() / Hide() | Reveals or hides the device in the world. |
| TeleportTo() / MoveTo() | Instantly or smoothly moves the device to a new position. |

🎠 Configuration Options (Details Panel)
* **Damage Multiplier**: How much to amplify damage (e.g., 2x = double damage).
* **Effect Duration**: How long the amplifier lasts after pickup (in seconds).
* **Infinite Effect Duration**: Effect lasts forever if enabled.
* **Respawn**: Whether the powerup respawns after use, and the cooldown for respawns.
* **Pickup Radius**: How close a player must be to pick up the powerup.
* **Selected Class/Team**: Restricts which class or team can pick up/use the powerup.
* **Apply To**: Who receives the effect (Only collector, whole team, etc.).
* **Appearance/Sounds/FX**: Configure visuals/audio shown during usage and pickup.
* **Enable at Game Start**: Whether the device is available at game start.
* **Visibility**: Device visibility and collision control.

🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use damage_amplifier_powerup_device
damage_amplifier_example := class(creative_device):

    @editable
    DamageAmplifier : damage_amplifier_powerup_device = damage_amplifier_powerup_device{}

    @editable
    SetMagnitudeButton : button_device = button_device{}

    @editable
    SetDurationButton : button_device = button_device{}

    @editable
    SpawnButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        DamageAmplifier.ItemPickedUpEvent.Subscribe(OnPowerupPickedUp)
        SetMagnitudeButton.InteractedWithEvent.Subscribe(OnSetMagnitudePressed)
        SetDurationButton.InteractedWithEvent.Subscribe(OnSetDurationPressed)
        SpawnButton.InteractedWithEvent.Subscribe(OnSpawnPressed)

    OnPowerupPickedUp(Agent : agent) : void =
        Print("Damage amplifier powerup picked up by agent!")

    OnSetMagnitudePressed(Agent : agent) : void =
        DamageAmplifier.SetMagnitude(2.0)
        Print("Damage amplifier magnitude set to 2.0x!")

    OnSetDurationPressed(Agent : agent) : void =
        DamageAmplifier.SetDuration(10.0)
        Print("Damage amplifier duration set to 10 seconds!")

    OnSpawnPressed(Agent : agent) : void =
        DamageAmplifier.Spawn()
        Print("Damage amplifier spawned!")
```

**Explanation:**
* The script demonstrates how to set up a damage amplifier powerup, change its damage multiplier or duration dynamically, spawn it, and listen for pickups.
* Button devices are used to control these behaviors in-game for demo/testing purposes.
* You can expand this to trigger additional effects or award players on `ItemPickedUpEvent`.

👥 Step-by-Step Setup in UEFN
1. **Create the Verse Device**
   * Open Verse Explorer (Verse → Verse Explorer).
   * Right-click a folder, choose "Create New Verse File" (e.g., `damage_amplifier_example.verse`).
   * Click "Create Empty", paste the example code, and save.
   * Click "Verse → Build Verse Code" (or Ctrl+Shift+B) until “Build Succeeded”.

2. **Add Devices to Level**
   * Place your `damage_amplifier_example` Verse device into your level.
   * Place at least one `damage_amplifier_powerup_device` and up to three `button_device`s (for controlling magnitude, duration, and spawning).

3. **Assign @editable References**
   * In the Details panel for your Verse device, set:
     * `DamageAmplifier` → the placed `damage_amplifier_powerup_device`
     * `SetMagnitudeButton`, `SetDurationButton`, `SpawnButton` → your placed buttons

4. **Configure Powerup Device in Details Panel**
   * Adjust multiplier, duration, respawn logic, pickup radius, team/class settings, FX, audio, and other options as desired.

5. **Test the Setup**
   * Launch a session or push changes and play.
   * Use the buttons you placed to spawn the powerup, change its multiplier, and duration. Pick it up to see the `ItemPickedUpEvent` fire.

🧠 Best Practices
* Pair with FX/HUD messages to give clear powerup feedback to players.
* Use `.SetMagnitude` or `.SetDuration` via Verse to adjust the effect based on round, time, or objectives.
* For team-wide or event-driven powerups, use appropriate "Apply To" settings.
* Use `.HasEffect(agent)` and `.GetRemainingTime(agent)` to display amplifier status or restrict stacking.

❌ Common Issues & Fixes
| Issue | ❌ Wrong Example | ✅ Correct Example | Explanation |
|-------|--------------------|-----------------------|-------------|
| Not referencing device | Omitted `@editable` or didn’t set refs | Set all device references in Details panel | Required for Verse code to work |
| Powerup not respawning | No respawn setting or called `Despawn()` only | Enable respawn in Details, or call `Spawn()` | Respawn logic is Details or Verse driven |
| No event on pickup | Omitted subscription to event | `ItemPickedUpEvent.Subscribe(OnEventFn)` | Required for response to powerup pickup |
| Changing settings in wrong place | Tried to set multiplier via Details only after play | Use both Details panel and Verse for runtime change | Runtime vs. setup configuration |
| Not enabling at startup | Set “Enable at Game Start” to No, no `Enable()` in code | Use Details panel or call `Enable()` in Verse | Device must be enabled to interact |

**Note:**
* Combine these devices for custom powerup zones, event-activated “berserk” modes, or as miniboss rewards.
* All damage effects are temporary and only apply to damage dealt while the effect is active.

