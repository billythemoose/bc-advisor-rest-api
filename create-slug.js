import {success} from "./libs/response-lib";
import * as dynamoDbLib from "./libs/dynamodb-lib";

export async function main(event, context, callback) {
    for(var classItem in event.Subjects) {
        var tableInsert = {
            TableName: "bcadmin-slug",
            Item: {
                slug: event.Subjects[classItem].Slug,
                title: event.Subjects[classItem].Title,
                coursePrefixes: JSON.stringify(event.Subjects[classItem].CoursePrefixes)
            }
        };

        try {
            await dynamoDbLib.call("put", tableInsert);
        }
        catch (e){
            console.log(e);
        }
    }

    return success({status: true});
}