from apify_client import ApifyClient

apify_client = ApifyClient('apify_api_hQOsWexa2Nw782SeXsUZhNmYjFqZuf197bgI')

# Start an actor and waits for it to finish
actor_call = apify_client.actor('mstephen190/proxy-scraper').call()

# Fetch results from the actor's default dataset
dataset_items = apify_client.dataset(actor_call['defaultDatasetId']).list_items().items
build=apify_client.builds()
print(apify_client.log(build_or_run_id=build))
for i in dataset_items:
    print(i)