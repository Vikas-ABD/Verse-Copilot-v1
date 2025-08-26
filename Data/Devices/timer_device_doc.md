📘 timer_device – UEFN Verse Device Documentation

🔹 Description
The `timer_device` lets you track time in your experience—counting up or down, displaying timers for players or globally, handling scoreboard logic, triggering events when time is up, or acting as a stopwatch for objectives. It's ideal for speedruns, round timers, puzzle countdowns, or any scenario where you need to start, pause, resume, or reset a timer in code or through gameplay.

🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `timer_device`

🎛 Device Options (Details Panel)
| Option Name | Description |
|-------------|-------------|
| Duration | Total time in seconds/minutes for countdown or stopwatch. |
| Count Down Direction | Count Down (to zero) or Count Up (from zero). |
| Start at Game Start | Whether the timer auto-starts when game begins. |
| Can Interact | Determines if/when players can interact to start/complete/pause/etc. |
| Applies To | Timer is global, or per-player. |
| Success On Timer End | Does reaching zero (or limit) count as success? |
| Completion Behavior | Reset, Stop, Restart, or Disable when the timer ends. |
| Visible During Game | Whether players can see the timer or its effects. |
| ...more options | Explore Details for color, team, FX, HUD display, etc. |

🛠️ Main Functions & Methods
- `Start(agent)` / `Start()` – Begins timer for given agent or globally.
- `Pause(agent)` / `Pause()` – Pauses the running timer for agent/all.
- `Resume(agent)` / `Resume()` – Resumes previously paused timer.
- `Reset(agent)` / `Reset()` – Resets timer to default duration.
- `Complete(agent)` / `Complete()` – Instantly finishes current timer, fires appropriate event.
- `Enable(agent)` / `Enable()` – Enables device (responds to triggers/Verse).
- `Disable(agent)` / `Disable()` – Disables device (ignores triggers/Verse).
- `SetActiveDuration(float)` – Sets current time remaining.
- `GetActiveDuration()` – Gets current time remaining.
- `SetMaxDuration(float)` – Sets total duration before end.
- `GetMaxDuration()` – Reads maximum duration.
- `IsStatePerAgent()` – Returns true if timer is tracked for each agent.

🧹 Events (Data Members)
- `SuccessEvent : listenable(?agent)` – Triggered when timer completes with success.
- `FailureEvent : listenable(?agent)` – Triggered when timer completes with failure.
- `StartUrgencyModeEvent : listenable(?agent)` – When timer enters “urgency” (low time, if used).

🧪 Verse Example: Timer Control & Event Handling
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

timer_state := enum:
	Stopped
	Running
	Paused

timer_device_example := class(creative_device):
	@editable
	Timer : timer_device = timer_device{}

	@editable
	StartButton : button_device = button_device{}
	@editable
	PauseButton : button_device = button_device{}
	@editable
	ResumeButton : button_device = button_device{}
	@editable
	ResetButton : button_device = button_device{}

	var CurrentState : timer_state = timer_state.Stopped

	OnBegin<override>()<suspends> : void =
		Timer.SuccessEvent.Subscribe(OnTimerSuccess)
		Timer.FailureEvent.Subscribe(OnTimerFailure)

		StartButton.InteractedWithEvent.Subscribe(OnStart)
		PauseButton.InteractedWithEvent.Subscribe(OnPause)
		ResumeButton.InteractedWithEvent.Subscribe(OnResume)
		ResetButton.InteractedWithEvent.Subscribe(OnReset)

	OnTimerSuccess(Agent : ?agent) : void =
		Print("Timer completed successfully!")
		set CurrentState = timer_state.Stopped

	OnTimerFailure(Agent : ?agent) : void =
		Print("Timer failed to complete.")
		set CurrentState = timer_state.Stopped

	OnStart(Agent : agent) : void =
		if (CurrentState = timer_state.Stopped):
			Timer.Start()
			set CurrentState = timer_state.Running
			Print("Timer started")

	OnPause(Agent : agent) : void =
		if (CurrentState = timer_state.Running):
			Timer.Pause()
			set CurrentState = timer_state.Paused
			Print("Timer paused")

	OnResume(Agent : agent) : void =
		if (CurrentState = timer_state.Paused):
			Timer.Resume()
			set CurrentState = timer_state.Running
			Print("Timer resumed")

	OnReset(Agent : agent) : void =
		Timer.Reset()
			set CurrentState = timer_state.Stopped
			Print("Timer reset")
```

📋 How to Use in UEFN
1. **Place Devices**
   - Drag a `timer_device` and four `button_devices` into your world (Start, Pause, Resume, Reset).
2. **Configure via Details**
   - Set duration, count direction, completion behavior, visibility.
3. **Set Up Your Verse Device**
   - In Verse Explorer: right-click a folder → Create New Verse File (e.g., `timer_device_example.verse`).
   - Paste code, save, then Build (Ctrl+Shift+B).
4. **Assign Device References**
   - Drag custom Verse device into level.
   - In Details: set `Timer`, `StartButton`, `PauseButton`, etc.
5. **Test**
   - Launch session, use buttons to control timer, see success/failure events.

🤔 Tips & Best Practices
- Use **per-agent** mode for personal challenges.
- Enable **urgency** mode for late-timer warning FX.
- Use `.Subscribe()` for event handlers.
- Combine with score trackers, logic devices for gameplay.

❌ Common Issues & Solutions
| Issue | Problem | Solution |
|-------|---------|----------|
| Timer won’t start | Not enabled/incorrect mode | Use `Enable()`, set "Start at Game" |
| Events not firing | Not subscribed in Verse | Use `.Subscribe()` for events |
| Timer not visible | Hidden in settings | Enable "Visible During Game" |

📅 Note
- All functionality can be triggered mid-game via Verse.
- Use with other devices for puzzles, races, rounds.
- Best for competitive or time-based experiences.

