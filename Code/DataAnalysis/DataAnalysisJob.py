example_dataanalysisjobs_json = { 
        "model_analysis_params" : {
            # Model to analyze each doc -> DocAnalysis
            "doc_analysis_model"            : "haiku",
            # "doc_chunk_size"                : 10_000,  # breaks up large documents into several chunks

            # Model to recursively stitch together DocAnalysis objects -> [DocAnalysis, DocAnalysis ...] -> DocAnalysis
            # Do this until there are less than {max_compilations_per_final_report} DocAnalysis objects left
            "recursive_compilation_model"   : "sonnet",
            "max_docs_per_compilation"      : 3, # only stitches max of 3 together at once

            # Model to generate final report out of DocAnalysis objects
            "final_report_model"            : "sonnet",
            "max_compilations_per_final_report" : 10, # => f(10 doc analyses) -> final report
        },
        "prompts" : {
            "doc_analysis_prompt" : "Analyze this doc, searching for xyz criteria.", # primary user input
            "doc_report_compilation_prompt" : "Combine these two reports", # recommended to not make this user input
            "final_report_prompt" : "Combine these reports into a final analysis with xyz criteria." # recommended to not make this user input
        },
        "excluded_directories" : [
            "/spotify", # example
        ]  #directories in /downloads/* to exclude from analysis
    }



# A request for data to be analyzed
# Essentially just a dictionary at the moment
class DataAnalysisJob():
    def __init__(self, data_analysis_jobs_json):
        self.use_rag = False
        self.model_analysis_params = data_analysis_jobs_json.get("model_analysis_params")
        
        # Extracting model parameters
        self.doc_analysis_model = self.model_analysis_params.get("doc_analysis_model")
        self.recursive_compilation_model = self.model_analysis_params.get("recursive_compilation_model")
        self.max_docs_per_compilation = self.model_analysis_params.get("max_docs_per_compilation")
        self.final_report_model = self.model_analysis_params.get("final_report_model")
        self.max_compilations_per_final_report = self.model_analysis_params.get("max_compilations_per_final_report")
        
        # Extracting prompts
        self.prompts = data_analysis_jobs_json.get("prompts")
        self.doc_analysis_prompt = self.prompts.get("doc_analysis_prompt")
        self.doc_report_compilation_prompt = self.prompts.get("doc_report_compilation_prompt")
        self.final_report_prompt = self.prompts.get("final_report_prompt")
        
        # Extracting excluded directories
        self.excluded_directories = data_analysis_jobs_json.get("excluded_directories")

    def __str__(self):
        return (f"DataAnalysisJob configured with:\n"
                f"Document Analysis Model: {self.doc_analysis_model}\n"
                f"Recursive Compilation Model: {self.recursive_compilation_model}\n"
                f"Max Docs Per Compilation: {self.max_docs_per_compilation}\n"
                f"Final Report Model: {self.final_report_model}\n"
                f"Max Compilations Per Final Report: {self.max_compilations_per_final_report}\n"
                f"Prompts: {self.prompts}\n"
                f"Excluded Directories: {self.excluded_directories}")
    
