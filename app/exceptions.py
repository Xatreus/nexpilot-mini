import exceptions


class Nexpilot(exceptions):
    repository_error: str = "Error analyzing repository"
    database_error: str = "Error searching documentation"
    llm_error: str = "Error generating response from LLM"


class repositoryError(Nexpilot):
    
