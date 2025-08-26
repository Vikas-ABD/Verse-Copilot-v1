import React, { useState, useRef, useEffect } from "react";

// Helper component to render the structured game plan
const GamePlanDisplay = ({ summary }: { summary: any }) => {
  if (!summary) return null;

  const TitledList = ({ title, items }: { title: string; items: string[] }) => (
    <div className="mt-4">
      <h3 className="text-lg font-semibold text-gray-700">{title}</h3>
      <ul className="list-disc list-inside pl-4 mt-2 space-y-1">
        {items?.map((item, index) => (
          <li key={index}>
            <code className="bg-gray-200 text-gray-800 px-2 py-1 rounded text-sm">{item}</code>
          </li>
        ))}
      </ul>
    </div>
  );

  return (
    <div className="bg-white rounded-2xl shadow-xl p-8 mt-6">
      <h2 className="text-2xl font-bold text-gray-800 border-b pb-2 mb-4">
        ✅ Game Plan Generated
      </h2>

      {/* Section 1: High-Level Plan */}
      <div className="mb-6">
        <h3 className="text-xl font-semibold text-gray-700">High-Level Game Plan & Architecture</h3>
        <p className="mt-2 text-gray-600"><strong>Core Gameplay Loop:</strong> {summary.highLevelGamePlanAndArchitecture?.coreGameplayLoop}</p>
        <p className="mt-2 text-gray-600"><strong>Proposed Architecture:</strong> {summary.highLevelGamePlanAndArchitecture?.proposedArchitecture}</p>
      </div>

      {/* Section 2: Asset List */}
      <div className="mb-6">
        <h3 className="text-xl font-semibold text-gray-700">Asset & Component List</h3>
        <TitledList title="Custom Verse Files" items={summary.assetAndComponentList?.customVerseFiles} />
        <TitledList title="Built-in Scene Graph Components" items={summary.assetAndComponentList?.builtInSceneGraphComponents} />
        <TitledList title="Required UEFN Devices" items={summary.assetAndComponentList?.requiredUefnDevices} />
      </div>

      {/* Section 3: Game Flow */}
      <div className="mb-6">
        <h3 className="text-xl font-semibold text-gray-700">Game Flow Explanation</h3>
        <pre className="bg-gray-100 p-4 rounded mt-2 text-gray-800 whitespace-pre-wrap font-sans text-sm">{summary.gameFlowExplanation}</pre>
      </div>

      {/* Section 4: Agent Questions */}
      <div>
        <h3 className="text-xl font-semibold text-gray-700">Step-by-Step Agent Questions</h3>
        {summary.stepByStepAgentQuestions?.map((item: any, index: number) => (
          <div key={index} className="mt-4 border-t pt-4">
            <h4 className="font-bold text-md text-gray-800">
              <code>{item.fileName}</code>
            </h4>
            <pre className="bg-gray-800 text-white p-4 rounded mt-2 whitespace-pre-wrap font-mono text-sm">{item.question}</pre>
          </div>
        ))}
      </div>
    </div>
  );
};


const API_URL = import.meta.env.VITE_API_URL;
const WS_URL = import.meta.env.VITE_WS_URL;

if (!API_URL || !WS_URL) {
  throw new Error("Environment variables VITE_API_URL and VITE_WS_URL must be set");
}

const API_ENDPOINT = `${API_URL}/generate-code`;
const WS_URL_TEMPLATE = `${WS_URL}/ws/status/`;
const ADD_KNOWLEDGE_ENDPOINT = `${API_URL}/add-knowledge1`;
const ADD_VIDEO_ENDPOINT = `${API_URL}/summarize-youtube-video`;

const WebSocketClient: React.FC = () => {
  const [editedQuestions, setEditedQuestions] = useState<string[]>([]); // Replaced 'question' state
  const [verseCode, setVerseCode] = useState<string>("");
  const [youtube_url, setVideoUrl] = useState<string>("");
  const [generatedCodes, setGeneratedCodes] = useState<string[]>([]);
  const [currentCodeViewIndex, setCurrentCodeViewIndex] = useState<number>(0);
  const [gamePlanData, setGamePlanData] = useState<any | null>(null);
  
  const [isGeneratingCode, setIsGeneratingCode] = useState<boolean>(false);
  const [isAddingKnowledge, setIsAddingKnowledge] = useState<boolean>(false);
  const [isAddingVideo, setIsAddingVideo] = useState<boolean>(false);
  
  const [copied, setCopied] = useState<boolean>(false);
  const [showVerseInput, setShowVerseInput] = useState<boolean>(false);
  const [showVideoInput, setShowVideoInput] = useState<boolean>(false);
  const [message, setMessage] = useState<string>("");
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState<number>(0);

  const inputRef = useRef<HTMLTextAreaElement | null>(null);

  const handleSubmit = async () => {
    const currentQuestionText = editedQuestions[currentQuestionIndex];
    if (!currentQuestionText || !currentQuestionText.trim()) return;

    setIsGeneratingCode(true);
    setMessage("");

    setGeneratedCodes(prevCodes => {
        const updatedCodes = [...prevCodes];
        updatedCodes[currentQuestionIndex] = ""; 
        return updatedCodes;
    });

    try {
      const res = await fetch(API_ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_question: currentQuestionText }),
      });

      const data = await res.json();
      const job_id = data?.job_id;
      if (!job_id) throw new Error("No job_id returned from backend");

      const ws = new WebSocket(`${WS_URL_TEMPLATE}${job_id}`);

      ws.onmessage = (event: MessageEvent) => {
        const msg = JSON.parse(event.data);
        if (msg.type === "final_result") {
          const newCode = msg.data?.final_code || "⚠️ No code returned";
          setGeneratedCodes(prev => {
              const newCodes = [...prev];
              newCodes[currentQuestionIndex] = newCode;
              return newCodes;
          });
          setCurrentCodeViewIndex(currentQuestionIndex);
          ws.close();
        } else if (msg.type === "error") {
          const errorMessage = "❌ Error: " + JSON.stringify(msg.data);
          setGeneratedCodes(prev => {
              const newCodes = [...prev];
              newCodes[currentQuestionIndex] = errorMessage;
              return newCodes;
          });
          setCurrentCodeViewIndex(currentQuestionIndex);
          ws.close();
        }
      };

      ws.onclose = () => setIsGeneratingCode(false);
      ws.onerror = () => {
        const errorMessage = "❌ WebSocket error occurred.";
        setGeneratedCodes(prev => {
            const newCodes = [...prev];
            newCodes[currentQuestionIndex] = errorMessage;
            return newCodes;
        });
        setCurrentCodeViewIndex(currentQuestionIndex);
        setIsGeneratingCode(false);
      };
    } catch (error) {
      console.error("Job start failed:", error);
      const errorMessage = "❌ Failed to start job. Please check the backend.";
       setGeneratedCodes(prev => {
            const newCodes = [...prev];
            newCodes[currentQuestionIndex] = errorMessage;
            return newCodes;
        });
      setCurrentCodeViewIndex(currentQuestionIndex);
      setIsGeneratingCode(false);
    }
  };

  const handleAddKnowledge = async () => {
    const currentQuestionText = editedQuestions[currentQuestionIndex];
    if (!currentQuestionText || !currentQuestionText.trim() || !verseCode.trim()) return;
    
    setIsAddingKnowledge(true);
    setMessage("");

    try {
      const response = await fetch(ADD_KNOWLEDGE_ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          question: currentQuestionText,
          verse_code: verseCode,
        }),
      });
      const result = await response.json();
      if (response.ok && result.status === "success") {
        setMessage("✅ Knowledge added successfully.");
        setTimeout(() => setMessage(""), 5000);
        setShowVerseInput(false);
        setVerseCode("");
      } else {
        setMessage(`⚠️ Failed: ${result?.detail || "Unknown error."}`);
      }
    } catch (error) {
      console.error("Error in add-knowledge:", error);
      setMessage("❌ Request failed. Check the server.");
    } finally {
      setIsAddingKnowledge(false);
    }
  };

  const handleAddVideo = async () => {
    if (!youtube_url.trim()) return;
    setIsAddingVideo(true);
    setGamePlanData(null);
    setMessage("");
    try {
      const response = await fetch(ADD_VIDEO_ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          youtube_url: youtube_url,
        }),
      });

      const result = await response.json();
      if (response.ok) {
        const summary = result?.summary;
        setGamePlanData(summary);
        
        // Initialize the editable questions state from the new plan
        if (summary?.stepByStepAgentQuestions) {
            const initialQuestions = summary.stepByStepAgentQuestions.map((q: any) => q.question);
            setEditedQuestions(initialQuestions);
        } else {
            setEditedQuestions([]);
        }

        setCurrentQuestionIndex(0);
        setGeneratedCodes([]);
        setCurrentCodeViewIndex(0);
      } else {
        setMessage(`⚠️ Failed: ${result?.detail || "Unknown error."}`);
      }
    } catch (error) {
      console.error("Error in add-video:", error);
      setMessage("❌ Request failed. Check the server.");
    } finally {
      setIsAddingVideo(false);
      setShowVideoInput(false);
      setVideoUrl("");
    }
  };
  
  const handleNextQuestion = () => {
    if (gamePlanData?.stepByStepAgentQuestions) {
        const totalQuestions = gamePlanData.stepByStepAgentQuestions.length;
        setCurrentQuestionIndex(prevIndex => Math.min(prevIndex + 1, totalQuestions - 1));
    }
  };

  const handlePreviousQuestion = () => {
    setCurrentQuestionIndex(prevIndex => Math.max(prevIndex - 1, 0));
  };

  const handleNextCode = () => {
      const totalQuestions = gamePlanData?.stepByStepAgentQuestions?.length || 0;
      setCurrentCodeViewIndex(prev => Math.min(prev + 1, totalQuestions -1));
  };

  const handlePreviousCode = () => {
      setCurrentCodeViewIndex(prev => Math.max(prev - 1, 0));
  };

  const handleCopy = () => {
    const codeToCopy = generatedCodes[currentCodeViewIndex];
    if (codeToCopy) {
      navigator.clipboard.writeText(codeToCopy).then(() => {
        setCopied(true);
        setTimeout(() => setCopied(false), 1500);
      });
    }
  };

  const hasQuestions = gamePlanData?.stepByStepAgentQuestions?.length > 0;
  const isFirstQuestion = currentQuestionIndex === 0;
  const isLastQuestion = hasQuestions && currentQuestionIndex === gamePlanData.stepByStepAgentQuestions.length - 1;

  const hasGeneratedCode = generatedCodes.length > 0 && generatedCodes.some(c => c);
  const isFirstCode = currentCodeViewIndex === 0;
  const isLastCode = hasQuestions && currentCodeViewIndex === gamePlanData.stepByStepAgentQuestions.length - 1;
  const currentCode = generatedCodes[currentCodeViewIndex];


  return (
    <div className="min-h-screen bg-gray-100 flex items-start justify-center px-4 py-10">
      <div className="w-full max-w-7xl grid md:grid-cols-2 gap-6">
        {/* Left Panel */}
        <div className="bg-white rounded-2xl shadow-xl p-8 space-y-6">
          <h1 className="text-4xl font-bold text-center text-gray-800">Verse Copilot</h1>
          <textarea
            ref={inputRef}
            value={editedQuestions[currentQuestionIndex] || ""}
            onChange={(e) => {
                const newEditedQuestions = [...editedQuestions];
                newEditedQuestions[currentQuestionIndex] = e.target.value;
                setEditedQuestions(newEditedQuestions);
            }}
            rows={3}
            placeholder="Enter your Verse code question"
            className="w-full resize-y px-4 py-2 rounded-lg border border-gray-300"
          />

          <div className="flex flex-col sm:flex-row gap-4 justify-start items-center flex-wrap">
            <button
              onClick={handleSubmit}
              disabled={isGeneratingCode}
              className={`px-6 py-2 rounded-lg text-white transition ${
                isGeneratingCode ? "bg-gray-400 cursor-not-allowed" : "bg-black hover:bg-gray-900"
              }`}
            >
              {isGeneratingCode ? "Thinking..." : "Submit"}
            </button>
            <button
              onClick={() => setShowVerseInput(true)}
              disabled={isAddingKnowledge}
              className="px-6 py-2 rounded-lg bg-indigo-600 text-white hover:bg-indigo-700 transition disabled:opacity-50"
            >
              Add Knowledge
            </button>
            <button
              onClick={() => setShowVideoInput(true)}
               disabled={isAddingVideo}
              className="px-6 py-2 rounded-lg bg-green-600 text-white hover:bg-green-700 transition disabled:opacity-50"
            >
              Add Video
            </button>
            
            {hasQuestions && (
                <div className="flex items-center gap-2">
                    <button 
                        onClick={handlePreviousQuestion}
                        disabled={isFirstQuestion}
                        className="px-3 py-2 rounded-lg bg-gray-200 text-gray-800 hover:bg-gray-300 disabled:opacity-50 disabled:cursor-not-allowed transition"
                    >
                        &larr;
                    </button>
                    <span className="text-sm text-gray-600">
                       {currentQuestionIndex + 1} / {gamePlanData.stepByStepAgentQuestions.length}
                    </span>
                    <button 
                        onClick={handleNextQuestion}
                        disabled={isLastQuestion}
                        className="px-3 py-2 rounded-lg bg-gray-200 text-gray-800 hover:bg-gray-300 disabled:opacity-50 disabled:cursor-not-allowed transition"
                    >
                        &rarr;
                    </button>
                </div>
            )}

          </div>

          {showVerseInput && (
            <div className="space-y-4">
              <textarea
                value={verseCode}
                onChange={(e) => setVerseCode(e.target.value)}
                rows={4}
                placeholder="Enter Verse code"
                className="w-full resize-y px-4 py-2 rounded-lg border border-gray-300"
              />
              <div className="flex justify-between">
                <button onClick={handleAddKnowledge} disabled={isAddingKnowledge} className={`px-4 py-2 rounded-lg text-white transition ${isAddingKnowledge ? "bg-gray-400" : "bg-indigo-600 hover:bg-indigo-700"}`}>
                  {isAddingKnowledge ? "Adding..." : "Add"}
                </button>
                <button onClick={() => setShowVerseInput(false)} className="text-sm text-red-600 hover:text-red-800">
                  Cancel
                </button>
              </div>
            </div>
          )}

          {showVideoInput && (
            <div className="space-y-4">
              <input type="text" value={youtube_url} onChange={(e) => setVideoUrl(e.target.value)} placeholder="Enter Video URL" className="w-full px-4 py-2 rounded-lg border border-gray-300"/>
              <div className="flex justify-between">
                <button onClick={handleAddVideo} disabled={isAddingVideo} className={`px-4 py-2 rounded-lg text-white transition ${isAddingVideo ? "bg-gray-400" : "bg-green-600 hover:bg-green-700"}`}>
                  {isAddingVideo ? "Adding..." : "Add Video"}
                </button>
                <button onClick={() => setShowVideoInput(false)} className="text-sm text-red-600 hover:text-red-800">
                  Cancel
                </button>
              </div>
            </div>
          )}

          {message && (<p className="text-sm font-medium text-blue-600 text-center transition duration-300">{message}</p>)}
          {gamePlanData && <GamePlanDisplay summary={gamePlanData} />}
        </div>

        {/* Right Panel */}
        {hasGeneratedCode && (
          <div className="bg-white rounded-2xl shadow-xl p-8 flex flex-col h-fit">
            <div className="flex items-center justify-between mb-4 gap-4">
              <h2 className="text-xl font-semibold text-gray-800">✨ Generated Verse Code</h2>
              <div className="flex items-center gap-2">
                {hasQuestions && (
                    <>
                        <button onClick={handlePreviousCode} disabled={isFirstCode} className="px-3 py-1 rounded-lg bg-gray-200 text-gray-800 hover:bg-gray-300 disabled:opacity-50 disabled:cursor-not-allowed transition">&larr;</button>
                        <span className="text-sm text-gray-600 whitespace-nowrap">
                            Code for Q {currentCodeViewIndex + 1}
                        </span>
                        <button onClick={handleNextCode} disabled={isLastCode} className="px-3 py-1 rounded-lg bg-gray-200 text-gray-800 hover:bg-gray-300 disabled:opacity-50 disabled:cursor-not-allowed transition">&rarr;</button>
                    </>
                )}
                <button onClick={handleCopy} disabled={!currentCode} className="text-sm bg-blue-600 text-white px-3 py-1 rounded hover:bg-blue-700 transition disabled:bg-gray-400">
                    {copied ? "✅ Copied!" : "Copy"}
                </button>
              </div>
            </div>
            <pre className="bg-gray-100 text-black p-4 rounded overflow-auto text-sm max-h-[600px] whitespace-pre-wrap">
              {currentCode || "No code generated for this question yet."}
            </pre>
          </div>
        )}
      </div>
    </div>
  );
};

export default WebSocketClient;