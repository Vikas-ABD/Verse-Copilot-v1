#import google.generativeai as genai
from google import genai
from google.genai import types
client = genai.Client()
import json
import os
from dotenv import load_dotenv

# Load environment variables at the earliest possible moment
load_dotenv()

class YouTubeSummarizationService:
    def __init__(self):
        # It's good practice to have the API key check here
        if not os.getenv("GOOGLE_API_KEY"):
            raise ValueError("GEMINI_API_KEY environment variable not set.")
        
    async def process_gemini_response(self,response_text: str) -> dict:
        """
        Cleans a string response from the Gemini API by removing Markdown code block wrappers,
        then parses it into a Python dictionary.

        Args:
            response_text: The raw string response from the API.

        Returns:
            A dictionary parsed from the JSON content.
            
        Raises:
            ValueError: If the response does not contain a valid JSON object.
            json.JSONDecodeError: If the extracted string is not valid JSON.
        """
        # Find the start of the JSON object
        start_index = response_text.find('{')
        # Find the end of the JSON object
        end_index = response_text.rfind('}')

        if start_index == -1 or end_index == -1:
            raise ValueError("Could not find a valid JSON object in the response string.")

        # Extract the JSON string
        json_string = response_text[start_index : end_index + 1]

        # Parse the cleaned string into a Python dictionary
        try:
            parsed_json = json.loads(json_string)
            return parsed_json
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            # Re-raise the exception to be handled by the calling code
            raise


    async def summarize_video(self, youtube_url: str) -> str:
        """
        Generates a summary for a given YouTube video URL using the Gemini API.

        Args:
            youtube_url: The public URL of the YouTube video.

        Returns:
            The generated summary as a string.
        """
        print(f"Attempting to summarize YouTube URL: {youtube_url}")

        # The system prompt that instructs the mode
        try:
            response = await client.aio.models.generate_content(
                        model='models/gemini-2.5-pro-preview-05-06',
                        contents=types.Content(
                            parts=[
                                types.Part(
                                    file_data=types.FileData(file_uri=youtube_url)
                                ),
                                types.Part(text="""You are an expert UEFN game designer and Verse programmer specializing in modern, component-based Scene Graph architecture.

Your input is a video that shows a complete, functional mini-game in Fortnite. You must observe all visuals, player actions, sound effects, and UI feedback.

Your goal is to analyze this video in meticulous detail and produce a complete development plan to recreate this game from scratch using a pure Scene Graph component-based workflow.

Response Generation Guidelines (Crucial):
Your entire response must be a single, detailed document that follows the five-section structure below. You must provide a complete plan that a developer or another AI agent can follow step-by-step to build the final, working game.

1. High-Level Game Plan & Architecture
Core Gameplay Loop: First, briefly describe the core gameplay loop you observe in the video.

Proposed Component-Based Architecture: Propose a decoupled, event-driven architecture using multiple custom components. Explain why this modular approach is superior for this project (mention reusability, scalability, and ease of debugging). Identify the primary custom Verse components that will be needed to build the game.

2. Asset & Component List
Provide a clear, itemized list of all the necessary assets and components, broken down into three categories:

Custom Verse Files: The names of the new .verse files we will create.

Built-in Scene Graph Components: The essential built-in components that will be used (e.g., mesh_component, sound_component).

Required UEFN Devices: Any traditional devices that are necessary to link systems together (e.g., a trigger_device or a billboard_device).

3. Game Flow Explanation
Describe the step-by-step flow of events for a single successful hit on a target.

Start from the moment the prop is damaged and end with the score being updated on the UI.

Clearly explain how the custom components will communicate with each other (e.g., "The target_component will signal its HitEvent, which the score_manager_component will be listening for.").

4. High-Quality Prompting Examples (Reference)
This section contains a complete, multi-file example project. You must use this as a "gold standard" to guide the structure and quality of the questions you generate in the next section. Pay close attention to how the questions create a sequence of interconnected components that work together to form a complete gameplay loop.

Example Project: The Collector's Room
This example shows how to build a complete gameplay loop where a player collects three coins to unlock a button, which then opens a door.

File 1: collectible_component.verse

Question:

"I need a robust, reusable Scene Graph component for a collectible item. Let's name it collectible_component.

It needs an @editable property for a door_button_component so it knows which button to notify when it's collected.

When a player touches the entity it's attached to, it should make the entity invisible and stop its animation.

After it disappears, it must call the public OnCoinCollected() function on the linked door_button_component.

After a 3-second delay, it must reappear and resume its animation.

Ensure all asynchronous logic is handled correctly with <suspends> and spawn."

Resulting Code:

using { /Verse.org/Simulation }
using { /Verse.org/SceneGraph }
using { /Verse.org/SceneGraph/KeyframedMovement }
using { /Verse.org/SpatialMath }
using { /Fortnite.com/Game }

collectible_component<public> := class<final_super>(component):
    @editable DoorButton:door_button_component = door_button_component{}
    @editable Keyframes:[]keyframed_movement_delta = array{}
    var StartTransform:transform = transform{}

    OnBeginSimulation<override>():void =
        (super:)OnBeginSimulation()
        if (FortRoundManager := Entity.GetFortRoundManager[]):
            FortRoundManager.SubscribeRoundStarted(OnRoundStarted)

    OnRoundStarted():void =
        set StartTransform = Entity.GetGlobalTransform()
        if (Mesh := Entity.GetComponent[mesh_component]):
            Mesh.EntityEnteredEvent.Subscribe(OnEntityEntered)
        spawn { PlayAnimation() }

    PlayAnimation()<suspends>:void =
        Entity.SetGlobalTransform(StartTransform)
        if (Mesh := Entity.GetComponent[mesh_component], Movement := Entity.GetComponent[keyframed_movement_component]):
            set Mesh.Visible = true
            Movement.SetKeyframes(Keyframes, loop_keyframed_movement_playback_mode{})
            Movement.Play()

    OnEntityEntered(OtherEntity:entity):void =
        spawn { OnEntityEntered_Async() }

    OnEntityEntered_Async()<suspends>:void =
        if (Mesh := Entity.GetComponent[mesh_component], Movement := Entity.GetComponent[keyframed_movement_component]):
            Movement.Stop()
            set Mesh.Visible = false
            DoorButton.OnCoinCollected()
            Sleep(3.0)
            spawn { PlayAnimation() }

File 2: door_component.verse

Question:

"I need a simple and efficient Scene Graph component to control a door. Name it door_component. When the game starts, it should find and save a reference to the keyframed_movement_component on the same entity. It also needs a public function called Open() that uses this saved reference to play the animation."

Resulting Code:

using { /Verse.org/SceneGraph }
using { /Verse.org/Simulation }
using { /Verse.org/SceneGraph/KeyframedMovement }

door_component<public> := class<final_super>(component):
    var MaybeAnimator: ?keyframed_movement_component = false

    OnBeginSimulation<override>():void =
        (super:)OnBeginSimulation()
        if (Animator := Entity.GetComponent[keyframed_movement_component]):
            set MaybeAnimator = option{Animator}

    Open<public>():void =
        if (Animator := MaybeAnimator?):
            Animator.Play()

File 3: door_button_component.verse

Question:

"Create the controller component named door_button_component.

It needs an @editable integer RequiredCoins and an @editable reference to the door prop entity.

Its own interactable_component must start disabled.

It needs a public function OnCoinCollected() that increments a counter. When the counter reaches RequiredCoins, it must enable its interactable_component.

When a player interacts with the button, it must find the door_component on the linked door prop and call its Open() function."

Resulting Code:

using { /Verse.org/SceneGraph }
using { /Verse.org/Simulation }

door_button_component<public> := class<final_super>(component):
    @editable DoorProp:entity = entity{}
    @editable RequiredCoins:int = 3
    var MaybeDoorComponent:?door_component = false
    var MaybeInteractable:?interactable_component = false
    var CoinsCollected:int = 0

    OnBeginSimulation<override>():void =
        (super:)OnBeginSimulation()
        if (DoorComponent := DoorProp.GetComponent[door_component]):
            set MaybeDoorComponent = option{DoorComponent}
        if (Interactable := Entity.GetComponent[interactable_component]):
            set MaybeInteractable = option{Interactable}
            Interactable.Disable()
            Interactable.SucceededEvent.Subscribe(OnInteract)

    OnCoinCollected<public>():void=
        set CoinsCollected += 1
        if (CoinsCollected >= RequiredCoins):
            if(Interactable := MaybeInteractable?):
                Interactable.Enable()

    OnInteract(Agent:agent):void =
        if (DoorComponent := MaybeDoorComponent?):
            DoorComponent.Open()

5. Step-by-Step Agent Questions
This is the most important section. Provide a sequence of precise, developer-style questions based on the high-quality examples above.

There must be exactly one question for each custom Verse file identified in your plan.

Each question must be a complete, self-contained prompt that contains all the information needed to generate the full code for that single file.

CRUCIAL RULE FOR CONTEXT: When one custom component needs to interact with another, you must use the correct Scene Graph communication pattern as shown in the examples. The question for a "listener" component must not ask it to redefine the "broadcaster" component. Instead, the question must instruct the agent to create an @editable property to reference the other component (or the entity it's attached to) and then specify that the code should call the public functions or subscribe to the public events of that referenced component. This ensures the final generated code will be interconnected and functional as a complete game.

The questions must also enforce best practices, such as caching component references in OnBeginSimulation for efficiency and correctly handling asynchronous logic with <suspends> and spawn.

NEW - CRUCIAL RULE FOR QUALITY: The questions you generate must be so precise and technically detailed that the final code-generating agent can produce a complete, build-ready script with no syntax errors. The questions must implicitly or explicitly guide the agent to include all necessary using statements, use correct event signatures (e.g., (Agent: agent) vs. (Result: damage_result)), and correctly handle failable expressions. The goal is to create prompts that prevent common errors from happening in the first place.
CRUCIAL RULE FOR MODULARITY: Each question you generate must result in a Verse file that defines only one custom component. The generated code for one component must never contain the class definition for another custom component from this plan. All communication between custom components must be handled through @editable references as shown in the examples.
important note is in a file we want only one component so if one file required other component to use we will use as editable entity and it was must cover in other file so the question you gave must be mention the context of this okkk. lets think deep deep deep...
CRUCIAL RULE FOR COMPONENT COMMUNICATION:
When one custom component needs to interact with another, the question you generate must enforce the correct, decoupled Scene Graph pattern.

The "listener" component must not have a direct @editable reference to the other custom component class (e.g., @editable Target: target_component is incorrect and forbidden).

Instead, the question must instruct the agent to create an @editable entity property to reference the prop that the other component is attached to.

The question must then specify that the code should get the custom component from that entity reference using GetComponent.

The question must not ask the agent to add a using statement for another custom component in the same project, as they exist in the same module and can see each other automatically.

Final Output Formatting (Crucial):

Your entire response must be a single, valid JSON object. Do not write any text, explanations, or markdown formatting (like ```json) outside of the main JSON object.

The JSON object must strictly adhere to the following structure. Fill in the values based on your analysis.

JSON Schema:

JSON

{
  "highLevelGamePlanAndArchitecture": {
    "coreGameplayLoop": "string",
    "proposedArchitecture": "string"
  },
  "assetAndComponentList": {
    "customVerseFiles": [
      "string"
    ],
    "builtInSceneGraphComponents": [
      "string"
    ],
    "requiredUefnDevices": [
      "string"
    ]
  },
  "gameFlowExplanation": "string",
  "stepByStepAgentQuestions": [
    {
      "fileName": "string",
      "question": "string"
    }
  ]
}
Adherence to this JSON schema is mandatory.
                                    
"""
 )
                            ]
                        )
                    )
            
            res = await self.process_gemini_response(response.text)
            # 3. Access the 'stepByStepAgentQuestions' and print them
            # questions = res.get("stepByStepAgentQuestions", [])

            # if not questions:
            #     print("No questions found in the response.")
            # else:
            #     print("--- Extracted Agent Questions ---")
            #     for i, item in enumerate(questions):
            #         file_name = item.get('fileName', 'N/A')
            #         question_text = item.get('question', 'No question text.')
            #         print(f"\n{i+1}. File Name: {file_name}")
            #         print(f"   Question: {question_text}")
            #     print("\n-------------------------------")

            return res
        except Exception as e:
            print(f"An error occurred while calling the Gemini API: {e}")
            # Re-raise or handle the exception as needed
            raise


#service = YouTubeSummarizationService()

async def process_youtube_url(youtube_url: str):
    """
    Initializes the service and calls the summarization method.
    This acts as a convenient entry point from the API route.
    """
    service = YouTubeSummarizationService()
    summary = await  service.summarize_video(youtube_url)
    return summary