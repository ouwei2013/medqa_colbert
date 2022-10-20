from colbert.data import Queries
from colbert.infra import Run, RunConfig, ColBERTConfig
from colbert import Searcher

if __name__=='__main__':
    with Run().context(RunConfig(nranks=1, experiment="medqa")):

        config = ColBERTConfig(
            root="./experiments",
        )
        searcher = Searcher(index="medqa_idx", config=config)

        query ='左手突然动不了，口嘴歪斜，这是什么病'
        results = searcher.search(query, k=10)

# Print out the top-k retrieved passages
        for passage_id, passage_rank, passage_score in zip(*results):
            print(f"\t [{passage_rank}] \t\t {passage_score:.1f} \t\t {searcher.collection[passage_id]}")
            # queries = Queries("/path/to/MSMARCO/queries.dev.small.tsv")
            # ranking = searcher.search_all(queries, k=100)
            # ranking.save("msmarco.nbits=2.ranking.tsv")