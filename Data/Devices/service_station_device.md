## service_station_device – UEFN Verse Device Documentation

### 🔹 Description
The `service_station_device` is an automated device in Unreal Editor for Fortnite (UEFN) designed to refuel and repair vehicles automatically. When a vehicle enters the station, it is refueled or repaired depending on its needs. Ideal for racing or driving maps, this device can be used as a gas station, repair bay, or maintenance checkpoint. Events can be handled in Verse, such as when vehicles enter/exit or start/finish repairs or fueling.

### 🧱 Imports Required
```verse
verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `service_station_device` (implements `healthful`, `damageable`, `enableable`)

### 🤝 Exposed Interfaces
| Interface   | Description                            |
|-------------|----------------------------------------|
| healthful   | Has health state; can be eliminated    |
| damageable  | Can take damage                        |
| enableable  | Can be enabled or disabled dynamically |

### 🧩 Data Members / Key Events
| Name                     | Type                          | Description                               |
|--------------------------|-------------------------------|-------------------------------------------|
| VehicleEnteredEvent      | listenable(fort_vehicle)      | Fires when a vehicle enters the station   |
| VehicleExitedEvent       | listenable(fort_vehicle)      | Fires when a vehicle exits the station    |
| VehicleFuelingBeginEvent | listenable(fort_vehicle)      | Fires when refueling starts               |
| VehicleFuelingEndEvent   | listenable(fort_vehicle)      | Fires when refueling ends                 |
| VehicleRepairBeginEvent  | listenable(fort_vehicle)      | Fires when repair begins                  |
| VehicleRepairEndEvent    | listenable(fort_vehicle)      | Fires when repair ends                    |
| DamagedEvent             | listenable(damage_result)     | Fires when station is damaged             |

### 🧰 Core Methods
| Method Signature                            | Description                                              |
|---------------------------------------------|----------------------------------------------------------|
| GetHealth(): float                          | Returns current health of the device                     |
| SetHealth(Health: float): void              | Sets health (must be >= 1.0)                            |
| GetMaxHealth(): float                       | Returns maximum possible health                         |
| SetMaxHealth(MaxHealth: float): void        | Sets max health and scales current health accordingly   |
| Damage(Amount: float): void                 | Damages the station anonymously                         |
| Damage(Args: damage_args): void             | Damages station with instigator/source info             |
| Enable(): void                              | Enables the device                                      |
| Disable(): void                             | Disables the device                                     |
| IsEnabled(): void (<decides>)               | Succeeds if enabled, fails if not                       |
| IsAnyVehicleInside(): void (<decides>)      | Succeeds if a vehicle is inside                         |
| MoveTo / TeleportTo / GetTransform          | Standard spatial functions                              |

### 📋 Configuration Options (Details Panel)
| Option                   | Values                     | Description                                            |
|--------------------------|-----------------------------|--------------------------------------------------------|
| Enabled on Game Start    | True / False                | Whether device is enabled at game start               |
| Overall Visual Style     | Default / Blank / Custom*   | Appearance customization                              |
| Paint Color / Icon / etc | Custom (conditional)        | Visual style and effects                              |
| Events                   | Device bindings             | Trigger external devices on station events            |
| Functions                | Bind station actions        | Bind Enable, Disable, CheckVehicle, etc.              |

### 🧰 Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

station_manager := class(creative_device):

    @editable
    Station : service_station_device = service_station_device{}

    OnBegin<override>()<suspends> : void =
        Station.VehicleEnteredEvent.Subscribe(OnVehicleIn)
        Station.VehicleFuelingBeginEvent.Subscribe(OnFuelingStart)
        Station.VehicleRepairBeginEvent.Subscribe(OnRepairingStart)
        Station.VehicleFuelingEndEvent.Subscribe(OnFuelDone)
        Station.VehicleRepairEndEvent.Subscribe(OnRepairDone)
        Station.VehicleExitedEvent.Subscribe(OnVehicleOut)

    OnVehicleIn(Vehicle: fort_vehicle):void =
        Print("A vehicle entered the station!")

    OnFuelingStart(Vehicle: fort_vehicle):void =
        Print("Refueling started.")

    OnRepairingStart(Vehicle: fort_vehicle):void =
        Print("Repair started.")

    OnFuelDone(Vehicle: fort_vehicle):void =
        Print("Vehicle refueled!")

    OnRepairDone(Vehicle: fort_vehicle):void =
        Print("Vehicle fully repaired!")

    OnVehicleOut(Vehicle: fort_vehicle):void =
        Print("Vehicle exited the station.")
```

### 🧠 Best Practices
- Always mark your `service_station_device` as `@editable` and assign it in the UEFN Details panel.
- Use event subscriptions to implement gameplay responses (e.g., rewards, VFX, sounds).
- Control activation via `Enable()` and `Disable()` for dynamic gameplay logic.
- Use health and damage methods for destructible gameplay setups.
- Configure style and effects using the visual options in the Details panel.

### ❌ Incorrect Usage Examples and Fixes
| Issue                             | ❌ Wrong Example         | ✅ Correct Example                  | Explanation                                          |
|----------------------------------|-----------------------------|----------------------------------------|------------------------------------------------------|
| Unset editable reference         | Using station without init | Assign device in Details panel         | Prevents nil access and runtime errors               |
| Setting health directly to 0     | SetHealth(0.0)             | Use Damage() instead                   | Cannot set health < 1.0 directly                     |
| Events not triggered             | Subscribed without enable  | Use Enable() method                    | Device must be enabled to function                  |

### ⚠️ Notes
- Repairing/refueling only occurs if needed.
- Use `IsAnyVehicleInside()` for advanced scripts like blocking areas.
- Configure all bindings in UEFN Details for a smoother editor experience.

