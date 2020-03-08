import * as dynamoDbLib from "./libs/dynamodb-lib";
import {success, failure} from "./libs/response-lib";

export async function main(event, context) {
    const params = {
        TableName: process.env.bcadminSlug
        // 'Key' defines the partition key and sort key of the item to be retrieved
        // - 'userId': Identity Pool identity id of the authenticated user
        // - 'quarterId': path parameter
    };

    try {
        const result = await dynamoDbLib.call("scan", params);
        if (result.Item) {
            return success(result.Item);
        }
        else if (result.Items) {
            return success(result.Items);
        }
        else {
            return failure({status: false, error: "Item not found"});
        }
    }
    catch (e) {
        console.log(e);
        return failure({status: false});
    }
}