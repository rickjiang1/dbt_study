SELECT
*
FROM {{ source('Landing', 'lnd_customer') }}