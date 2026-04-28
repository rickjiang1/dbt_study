SELECT
*,
'{{invocation_id}}' as run_ID
FROM {{ source('src_Landing', 'lnd_customer') }}