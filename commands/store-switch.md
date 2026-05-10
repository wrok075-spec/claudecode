Switch Shopify CLI connection to a different store.

Usage: /store-switch $ARGUMENTS

Arguments: A store alias (sky, kwinzii, tt) or "list" to show all stores, or "status" to check current connection.

Steps:

1. Read the stores config from /Users/eapple/.claude/stores.json
2. If argument is "list" or empty: show a table of all configured stores with alias, domain, and name. Then check which store is currently connected by running `shopify theme info 2>&1` and highlight it.
3. If argument is "status": run `shopify theme info 2>&1` to show the currently connected store.
4. If argument is a store alias (e.g., "sky", "kwinzii", "tt"):
   a. Look up the domain and scopes from stores.json
   b. ALWAYS run `shopify auth logout` first to clear any cached session — this prevents the CLI from redirecting to the wrong store during OAuth
   c. Run `shopify store auth --store {domain} --scopes {scopes}` to authenticate
   d. If auth requires interactive browser login, tell the user to run: `! shopify auth login` and then enter the store domain when prompted. Remind them to make sure they're logged into the correct Shopify account in their browser. If it redirects to the wrong store, they should first log out of Shopify at https://accounts.shopify.com/logout
   e. Verify connection with `shopify store execute --store {domain} --query 'query { shop { name } }'`
   f. Report success with the store name and domain
5. If argument is "add {alias} {domain} {name}": add a new store entry to stores.json
6. If the alias is not found, suggest the closest match from the available aliases.

Always show the result clearly — which store you're now connected to.
