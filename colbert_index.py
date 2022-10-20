from colbert.infra import Run, RunConfig, ColBERTConfig
from colbert import Indexer

if __name__=='__main__':
    with Run().context(RunConfig(experiment="medqa")):

        config = ColBERTConfig(
            nbits=2,
            root="./experiments"
        )
        indexer = Indexer(checkpoint="./experiments/medqa/none/2022-10/13/14.59.02/checkpoints/colbert", config=config)
        indexer.index(name="medqa_idx", collection="answers.tsv")