# real_time_clock_device – UEFN Verse Device Documentation

## 🔊 Description
The `real_time_clock_device` allows in-game events and actions to be linked directly to real-world time. With flexible triggers for date, hour, or duration, this device enables:
- Scheduled start/end times for events.
- Real-world day/night gameplay variations.
- Periodic recurring events synced to the real clock.

Supports countdowns, scheduled activations, recurring or persistent unlocks.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object` – Base class for all creative devices/props.
- `creative_device_base` – Base class for creative_device.
- `real_time_clock_device`

## 🧹 Data Members (Events)
| Name                              | Type                   | Description                                                            |
|-----------------------------------|------------------------|------------------------------------------------------------------------|
| `TimeReachedEvent`                | `listenable(tuple())`  | Fires when the target real-world time is reached.                      |
| `DurationElapsedEvent`           | `listenable(tuple())`  | Fires after a set *duration* from the target time.                     |
| `EnablingAfterTimeReachedEvent`  | `listenable(tuple())`  | Fires if the device is enabled *after* the target time has passed.     |
| `EnablingBeforeTimeReachedEvent` | `listenable(tuple())`  | Fires if the device is enabled *before* the target time arrives.       |

## 🛠️ Functions & Methods
| Name        | Description                       |
|-------------|-----------------------------------|
| `Enable()`  | Enables the device.               |
| `Disable()` | Disables the device.              |

Also supports standard movement/transform methods inherited from base classes.

## 🎮 Configuration Options (Details Panel)
| Option                    | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| `Clock Face Style`        | Visual style of the in-game countdown, if used.                            |
| `Minute / Hour / Day / Month / Year` | Set target real-world time.                                     |
| `Display Mode`            | Show date or countdown on HUD.                                            |
| `Duration Type/Value`     | Additional event fired after specified duration.                           |
| `Number of Repeats / Frequency` | Configure repeated event triggers (hourly, daily, etc.).           |
| `Enabled At Game Start`   | If checked, device auto-activates at game start.                           |
| `Time Zone`               | Only GMT is supported.                                                     |
| `Instigator For Event`    | Specifies who receives the events (e.g., All Players, No Instigator).      |

## 🛠️ Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

real_time_clock_example := class(creative_device):

    @editable
    Clock : real_time_clock_device = real_time_clock_device{}

    @editable
    DayEventTrigger : trigger_device = trigger_device{}

    @editable
    NightEventTrigger : trigger_device = trigger_device{}

    OnBegin<override>()<suspends> : void =
        # Enable the clock
        Clock.Enable()

        # Get current time values
        CurrentHour := Clock.GetHoursSinceEpoch()
        CurrentMinute := Clock.GetMinutesSinceEpoch()
        CurrentSecond := Clock.GetSecondsSinceEpoch()

        Print("Current time: {CurrentHour}:{CurrentMinute}:{CurrentSecond}")

        # Trigger events based on hour
        if (CurrentHour >= 6 and CurrentHour < 18):
            DayEventTrigger.Trigger()
        else:
            NightEventTrigger.Trigger()
```

## 🧠 Best Practices
- Always call `.Enable()` or set device to Enabled at Game Start.
- Listen for `TimeReachedEvent`, `DurationElapsedEvent`, etc.
- Use display mode for countdowns and match to GMT.
- Combine with triggers or Verse logic for complex scenarios.

## ❌ Incorrect Usage Examples
| Issue                      | ❌ Wrong                                  | ✅ Correct                                                 | Explanation                                                     |
|----------------------------|---------------------------------------------|---------------------------------------------------------------|-----------------------------------------------------------------|
| Not enabling the clock     | No call to `.Enable()`                      | Call `.Enable()` in Verse or set Enabled At Game Start         | Events won’t fire if clock is disabled.                         |
| Missing event subscriptions| No listeners attached                       | Subscribe to `.TimeReachedEvent`, etc.                         | Events must be handled explicitly in logic.                    |
| Expecting repeat w/o config| No repeat setup in Details                  | Configure "Number of Repeats / Frequency" in panel             | Events only fire once unless repetition is configured.         |
| Wrong timezone             | Using local time directly                   | Convert time to GMT before setting                            | Device time operates on GMT only.                             |

## 🧠 Notes
- Ideal for persistent and synchronized Fortnite islands.
- Real-world clock sync allows live events and global scheduling.
- Combine with triggers, Verse logic, and UI for engaging experiences.

