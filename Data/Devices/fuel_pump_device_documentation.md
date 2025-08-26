## fuel_pump_device – UEFN Verse Device Documentation

### 🔹 Description
The `fuel_pump_device` is used to provide fuel to vehicles in your Fortnite island. It supports infinite or limited fuel and can also act as a hazard by dealing damage to agents and the environment when destroyed or emptied. The device is configurable for team/class access, destructibility, scoring, and can be controlled dynamically using Verse scripting.

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `fuel_pump_device`

### 🧹 Data Members (Events)
| Name       | Type             | Description                                      |
|------------|------------------|--------------------------------------------------|
| EmptyEvent | listenable(agent) | Signals when the fuel pump is emptied by an agent. |

### 🛠️ Functions & Methods
| Name        | Description                                        |
|-------------|----------------------------------------------------|
| Enable()    | Enables the fuel pump device for agent interaction. |
| Disable()   | Disables the device; prevents all interaction/use.  |
| Reset()     | Resets fuel to its maximum (set by Fuel Capacity).  |
| Empty(agent)| Empties the pump, granting fuel to the given agent.|
| Show()      | Shows the pump in the world.                        |
| Hide()      | Hides the pump from the world.                      |
| GetTransform() | Gets the current transform (position, rotation, scale). |
| MoveTo()/TeleportTo() | Animates or teleports the pump to a different location. |

### 🎛 Configuration Options (Details Panel)
| Option                   | Description                                                           |
|--------------------------|-----------------------------------------------------------------------|
| Infinite Fuel            | On/Off – Unlimited or limited fuel stock.                              |
| Fuel Capacity            | Amount of fuel available if not infinite.                              |
| Indestructible           | Yes/No – Whether the pump can be damaged/destroyed.                    |
| Health                   | Damage it takes before destroyed (if indestructible is No).            |
| Explosion Deals Damage   | Yes/No – Exploding pump damages agents/environment.                     |
| Enabled At Game Start    | Enabled/Disabled.                                                      |
| Allowed Team/Class       | Who can access or use the device.                                      |
| Appearance/Name          | Custom display name, mesh, and visual options.                         |

*All configuration is set in the Details panel in UEFN.*

### 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

fuel_pump_example := class(creative_device):

    @editable
    FuelPump : fuel_pump_device = fuel_pump_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    ResetButton : button_device = button_device{}

    @editable
    EmptyButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        FuelPump.EmptyEvent.Subscribe(OnEmpty)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        ResetButton.InteractedWithEvent.Subscribe(OnResetPressed)
        EmptyButton.InteractedWithEvent.Subscribe(OnEmptyPressed)

    OnEmpty(Agent : agent) : void =
        Print("Fuel pump is empty!")

    OnEnablePressed(Agent : agent) : void =
        FuelPump.Enable()
        Print("Fuel pump enabled!")

    OnDisablePressed(Agent : agent) : void =
        FuelPump.Disable()
        Print("Fuel pump disabled!")

    OnResetPressed(Agent : agent) : void =
        FuelPump.Reset()
        Print("Fuel pump reset!")

    OnEmptyPressed(Agent : agent) : void =
        FuelPump.Empty(Agent)
        Print("Fuel pump emptied by agent!")
```

#### Explanation
- This example wires a `fuel_pump_device` with four `button_device`s for enabling, disabling, resetting, and manually emptying it.
- Listens to `EmptyEvent` and prints log outputs for each action.

### ✅ Step-by-Step Setup in UEFN
1. **Create the Verse Device**
   - Open Verse Explorer in UEFN.
   - Right-click a folder and select "Create New Verse File" (e.g., `fuel_pump_example.verse`).
   - Paste the code, save, and build (Ctrl+Shift+B) until "Build Succeeded".

2. **Add Devices to Your Level**
   - Place your `fuel_pump_example` Verse device into the level.
   - Place one `fuel_pump_device` and four `button_device`s for each control.

3. **Assign @editable References**
   - In the Details panel for the Verse device:
     - Assign `FuelPump` to your placed `fuel_pump_device`
     - Assign `EnableButton`, `DisableButton`, `ResetButton`, and `EmptyButton` accordingly

4. **Configure the Fuel Pump Device**
   - Set options like `Infinite Fuel`, `Health`, `Explosion Deals Damage`, etc., in the Details panel.

5. **Test Functionality**
   - Launch a play session.
   - Use the buttons to interact with the pump and observe printed logs.
   - If destructible and destroyed, verify that explosion and damage logic works.

### 🧠 Best Practices
- Enable "Indestructible: No" and "Explosion Deals Damage: Yes" to create hazards.
- Group multiple pumps for pit stops, checkpoints, or team play.
- Use `.Enable()`, `.Disable()`, `.Empty()` dynamically for events or win conditions.
- Leverage `EmptyEvent` for scoring, triggers, or chain reactions.

### ❌ Common Issues & Fixes
| Issue                   | ❌ Wrong Approach                          | ✅ Correct Approach                                         | Explanation                                           |
|------------------------|----------------------------------------------|--------------------------------------------------------------|-------------------------------------------------------|
| Not referencing device | Left @editable fields unassigned in Verse    | Assign devices in the Details panel                          | Required for Verse interaction                        |
| Device not interactable| Left disabled or not reset                   | Use `.Enable()` or `.Reset()` in Verse or via buttons        | Must be enabled and stocked for use                  |
| No explosion/damage    | Explosion/Damage not enabled in Details      | Set "Explosion Deals Damage" and "Indestructible: No"        | Needed for hazard gameplay                           |
| No empty event logic   | Did not subscribe to `EmptyEvent`            | Use `EmptyEvent.Subscribe(...)` to handle event              | Needed for scoring/reward logic                      |

**Note:**
- All item/fuel logic is configured via the Details panel or Verse calls.
- Device supports team/class restrictions and visual customization.
- Use in various gameplay modes like races, sabotage, or checkpoints.

