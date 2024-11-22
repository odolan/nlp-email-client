"use client";

import { useState } from "react";
import { classifyEmail, summarizeEmail } from "./api/api";
import { Loader2 } from 'lucide-react';

export default function Home() {

  const [inputText, setInputText] = useState("");
  const [classification, setClassification] = useState<string | null>(null);
  const [summary, setSummary] = useState<string | null>(null);
  const [summaryLoading, setSummaryLoading] = useState<boolean>(false);



  const handleClassify = async () => {
    console.log("Starting classification process...");
    console.log("Input text:", inputText);

    setSummaryLoading(true);

    try {
      const result = await classifyEmail(inputText);
      console.log("Classification result:", result);

      if ("classification" in result) {
        setClassification(result.classification);
      } else {
        console.log("Error in classification response:", result.error);
      }
    } catch (error) {
      console.error("Error during classification request:", error);
    } finally {
      setSummaryLoading(false);
    }
  };

  const handleReset = () => {
    setInputText("");
    setClassification(null);
    setSummary(null);
    setSummaryLoading(false);
  }

  const handleSummarize = () => {
    console.log("Starting summarization process...");
    console.log("Input text:", inputText);

    setSummaryLoading(true); // Start the loader

    summarizeEmail(inputText)
        .then((result) => {
            console.log("Summarization result:", result);

            if ("summary" in result) {
                setSummary(result.summary); // Update state with the summary
            } else {
                console.log("Error in summarization response:", result.error);
                setSummary("Failed to generate summary."); // Handle API error
            }
        })
        .catch((error) => {
            console.error("Error during summarization request:", error);
            setSummary("An error occurred while summarizing."); // Handle fetch error
        })
        .finally(() => {
            setSummaryLoading(false); // Stop the loader
        });
};


  return (
    <div className="items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
        <h1 className="text-4xl">👴🏻👵🏻 Email Client</h1>
        <textarea
          className="w-full border border-gray-300 p-4 rounded resize-none h-60 text-black"
          placeholder="Enter email text here..."
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
        ></textarea>

        <div className="flex gap-4">
          <button
            onClick={handleClassify}
            className="rounded-full border border-solid border-black/[.08] dark:border-white/[.145] transition-colors flex items-center justify-center hover:bg-[#f2f2f2] dark:hover:bg-[#1a1a1a] text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5"
          >
            Classify
          </button>

          <button
            onClick={handleSummarize}
            className="rounded-full border border-solid border-black/[.08] dark:border-white/[.145] transition-colors flex items-center justify-center hover:bg-[#f2f2f2] dark:hover:bg-[#1a1a1a] text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5"
          >
            Summarize
          </button>

          <button
            onClick={handleReset}
            className="rounded-full border border-solid border-[#FF0800] dark:border-white/[.145] transition-colors flex items-center justify-center text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5 bg-[#FFE4E1] text-[#FF0800]"
          >
            Reset
          </button>
        </div>

        { summaryLoading ? (
            <div className="flex items-center justify-center py-4">
              <Loader2 className="w-6 h-6 animate-spin text-blue-600" />
            </div>
          ) : summary ? (
            <div className="w-full border border-[#BF00FF] p-4 rounded bg-[#FAE6FA]">
              <h2 className="font-semibold text-[#BF00FF] mb-2">Summary</h2>
              <p className="text-[#DA70D6]">{summary}</p>
            </div>
          ) : <></>
        }

        {classification && (
          <div className="w-full border border-[#BF00FF] p-4 rounded bg-[#FAE6FA]">
            <h2 className="font-semibold text-[#BF00FF] mb-2">Classification</h2>
            <p className="text-[#DA70D6]">{classification}</p>
          </div>
        )}
      </main>
    </div>
  );
}
