from agent import extractive_summary


def test_extractive_summary_prefers_repeated_topic_terms():
    text = (
        "Vector databases store embedding vectors for semantic retrieval. "
        "Traditional databases are still useful for exact structured queries. "
        "Embedding vectors let applications compare semantic similarity. "
        "Vector search is commonly used in retrieval augmented generation systems. "
        "Semantic retrieval can find related meaning even when wording differs."
    )
    summary = extractive_summary(text, max_sentences=2).lower()
    assert "vector" in summary or "semantic" in summary
