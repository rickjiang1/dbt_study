SELECT
*,
'{{invocation_id}}' as run_ID
FROM {{ source('Landing', 'lnd_customer') }}