import {success} from "./libs/response-lib";
import * as dynamoDbLib from "./libs/dynamodb-lib";

export async function main(event, context, callback) {
    for(var classItem in event.Classes) {
        for(var item in event.Classes[classItem].Courses) {
            var tableInsert = {
                TableName: "bcadmin-classes",
                Item: {
                    slug: event.Classes[classItem].Courses[item].Subject,
                    id: event.Classes[classItem].Courses[item].Number,
                    title: event.Classes[classItem].Courses[item].Title,
                    quarter: event.Classes[classItem].CurrentQuarter.FriendlyName
                }
            };

            try {
                await dynamoDbLib.call("put", tableInsert);
            }
            catch (e){
                console.log(e);
            }
        }
    }

    return success({status: true});
}