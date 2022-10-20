from colbert.infra import Run, RunConfig, ColBERTConfig
from colbert import Trainer

if __name__=='__main__':
    with Run().context(RunConfig(experiment="medqa")):

        config = ColBERTConfig(
            bsize=32,
            root="./experiments",
        )
        trainer = Trainer(
            triples="triplets.jsonl",
            queries="questions.tsv",
            collection="answers.tsv",
            config=config,
        )

        checkpoint_path = trainer.train('bert-base-chinese')

        print(f"Saved checkpoint to {checkpoint_path}...")