from langchain.embeddings.base import Embeddings
from langchain.schema import BaseRetriever
from langchain.vectorstores import Chroma


class RedundantFilterRetriever(BaseRetriever):
    # make user pass in needed instance
    embeddings: Embeddings
    chroma: Chroma

    def get_relevant_documents(self, query):
        # calculate embeddings for the query
        emb = self.embeddings.embed_query(query)
        # take embeddings and feed them into that
        # max_marginal_relevance_search_by_vector
        return self.chroma.max_marginal_relevance_search_by_vector(
            embedding=emb,
            lambda_mult=0.8,
        )

    async def aget_relevant_documents(self, query):
        return []
