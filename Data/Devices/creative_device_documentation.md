📘 creative\_device – UEFN Verse Device Documentation

🔹 Description The creative\_device is the primary base class for creating custom interactive gameplay devices in Unreal Editor for Fortnite (UEFN) using Verse. By inheriting from creative\_device, you define new devices with custom behaviors, event logic, and dynamic interactions. All user-authored Verse devices (for puzzles, triggers, scoring, and more) are built as subclasses of creative\_device.

🧱 Imports Required Include these at the top of your Verse file for most interactions: verse using { /Fortnite.com/Devices } using { /Verse.org/Simulation } using { /UnrealEngine.com/Temporary/SpatialMath } using { /UnrealEngine.com/Temporary/Diagnostics }

🔁 Main Lifecycle Events

| Event           | Description                                          | Handler Signature     | Example Usage                               |
| --------------- | ---------------------------------------------------- | --------------------- | ------------------------------------------- |
| OnBegin()\:void | Called when your device is initialized at game start | OnBegin()\:void = ... | Initialize logic, subscribe to events, etc. |
| OnEnd()\:void   | Called when the experience ends                      | OnEnd()\:void = ...   | Cleanup logic                               |

🛠 Core Methods

| Method Signature                                                             | Description                                                       |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Enable(): void                                                               | Enables the device, making it active in game.                     |
| Disable(): void                                                              | Disables the device, hiding or deactivating it.                   |
| GetTransform(): transform                                                    | Retrieves the current position, rotation, and scale.              |
| MoveTo(Position: vector3, Rotation: rotation, Time: float): move\_to\_result | Smoothly moves the device to a new spot over time.                |
| MoveTo(TargetTransform: transform, Time: float): move\_to\_result            | Moves to a complete transform over time.                          |
| TeleportTo(Position: vector3, Rotation: rotation): void                      | Instantly teleports to a new position/rotation.                   |
| TeleportTo(TargetTransform: transform): void                                 | Instantly teleports to full transform (including scale).          |
| FindCreativeObjectsWithTag(Tag: tag): generator(creative\_object\_interface) | Returns all creative objects/devices with the given gameplay tag. |

🚦 Common Usage: Step-by-Step Example verse using { /Fortnite.com/Devices } using { /Verse.org/Simulation } using { /UnrealEngine.com/Temporary/SpatialMath } using { /UnrealEngine.com/Temporary/Diagnostics }

```
my_custom_device := class(creative_device):

@editable
Target : creative_device = creative_device{}

OnBegin<override>()<suspends> : void =
# Example: Move target device after 2 seconds
Sleep(2.0)
NewPosition := vector3{X := 500.0, Y := 100.0, Z := 200.0}
NewRotation := MakeRotation(vector3{X := 0.0, Y := 0.0, Z := 1.0}, 1.57) # 90 degrees
Target.MoveTo(NewPosition, NewRotation, 1.0)

# Print transform for debugging
CurrentTransform := Target.GetTransform()
Print("Target position: {CurrentTransform.Translation}")

# Enable/Disable example
EnableTarget() : void =
	Target.Enable()
DisableTarget() : void =
	Target.Disable()
```

❌ Incorrect Usage Examples and How to Fix

| Issue                     | ❌ Wrong Example                                    | ✅ Correct Example                         | Explanation                                     |
| ------------------------- | -------------------------------------------------- | ----------------------------------------- | ----------------------------------------------- |
| Wrong lifecycle usage     | Override other functions instead of OnBegin/OnEnd  | Use OnBegin()\:void                       | Only OnBegin and OnEnd get called automatically |
| No @editable reference    | Reference device in Verse but don't set in Details | Assign via @editable, then set in Details | Must assign device references inside the editor |
| Invalid use after disable | Use a device after it's disabled                   | Call Enable() before other methods        | Device must be enabled for most actions         |

🧬 Best Practices

- Always use @editable properties for devices you wish to control or reference.
- Use the OnBegin lifecycle event to initialize subscriptions, move devices, or set up state.
- Prefer MoveTo for smooth animations, TeleportTo for instant changes.
- Use GetTransform() for precise spatial manipulation or debugging.
- Leverage tags and FindCreativeObjectsWithTag for dynamic grouping or search.
- Always check validity (IsValid[]) if the device may have been destroyed or reset.

Great for:

- Scripting custom puzzles and logic
- Dynamic platforms or traps
- Complex event chains or triggers
- Creating manager objects for other Verse/game devices

