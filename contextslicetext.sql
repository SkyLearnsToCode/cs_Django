-- copy (
-- 	select row_to_json(t)
-- 	from (
-- 		select array_to_json(array_agg(row_to_json(d))) as nodes
-- 		from (
-- 			select entity_category as category, document_id as docid, ne.entity_name as name
-- 			from step3_name_entity ne inner join step3_document_entity de on ne.entity_name = de.entity_id
-- 			where document_id in ('se2', 'fib9', 'cia2')
-- 		) d
-- 		UNION ALL
-- 		select array_to_json(array_agg(row_to_json(s))) as contents 
-- 		from (
-- 			select "docText" as doctext, "docID" as docid
-- 			from step3_document
-- 			where "docID" in ('se2', 'fib9', 'cia2')
-- 		) s
-- 	) t
-- ) to '/Users/tianyili/Box Sync/VT/Academic/CrowdsourcedSensemaking/cs_django/step3/static/step3/test.json';

-- copy (
-- 	select array_to_json(array_agg(row_to_json(s))) as contents 
-- 	from (
-- 		select "docText" as doctext, "docID" as docid
-- 		from step3_document
-- 		where "docID" in ('se2', 'fib9', 'cia2')
-- 	) s
-- ) to '/Users/tianyili/Box Sync/VT/Academic/CrowdsourcedSensemaking/cs_django/step3/static/step3/test.json';

copy (
	select json_build_object(
		'nodes', (
					select array_to_json(array_agg(row_to_json(d))) as nodes
					from (
						select entity_category as category, document_id as docid, ne.entity_name as name
						from step3_name_entity ne 
						inner join step3_document_entity de on ne.entity_name = de.entity_id
						where document_id in ('se2', 'fbi9', 'cia2')
					) d
			),
		'contents', (
					select array_to_json(array_agg(row_to_json(s))) as contents 
					from (
						select "docText" as doctext, "docID" as docid
						from step3_document
						where "docID" in ('se2', 'fbi9', 'cia2')
					) s
			),
		'links', json_build_object()
		)
	from step3_document
	where "docID" = 'se2'
) to '/Users/tianyili/Box Sync/VT/Academic/CrowdsourcedSensemaking/cs_django/step3/static/step3/test.json'
WITH CSV QUOTE E'\t';