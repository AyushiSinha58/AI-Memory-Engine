-- CREATE DATABASE memory_engine;
-- USE memory_engine;

CREATE INDEX idx_content ON memory(content);
CREATE INDEX idx_importance ON memory(importance_score);

CREATE TABLE IF NOT EXISTS memory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT,
    type VARCHAR(50),
    importance_score FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    frequency INT DEFAULT 1
);

SET SQL_SAFE_UPDATES = 0;

DELETE t1 FROM memory t1
JOIN memory t2
ON t1.content = t2.content
AND t1.id > t2.id;

SELECT content, importance_score
FROM memory
ORDER BY importance_score DESC
LIMIT 100;