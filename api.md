# Shared Types

```python
from omnistack.types import ProjectAPIKey, ProjectServiceAccount, ProjectUser
```

# Chats

## Completions

Types:

```python
from omnistack.types.chats import CompletionCreateResponse
```

Methods:

- <code title="post /chat/completions">client.chats.completions.<a href="./src/omnistack/resources/chats/completions.py">create</a>(\*\*<a href="src/omnistack/types/chats/completion_create_params.py">params</a>) -> <a href="./src/omnistack/types/chats/completion_create_response.py">CompletionCreateResponse</a></code>

# Completions

Types:

```python
from omnistack.types import CompletionCreateResponse
```

Methods:

- <code title="post /completions">client.completions.<a href="./src/omnistack/resources/completions.py">create</a>(\*\*<a href="src/omnistack/types/completion_create_params.py">params</a>) -> <a href="./src/omnistack/types/completion_create_response.py">CompletionCreateResponse</a></code>

# Images

Types:

```python
from omnistack.types import ImageResponse
```

## Generations

Methods:

- <code title="post /images/generations">client.images.generations.<a href="./src/omnistack/resources/images/generations.py">create</a>(\*\*<a href="src/omnistack/types/images/generation_create_params.py">params</a>) -> <a href="./src/omnistack/types/image_response.py">ImageResponse</a></code>

## Edits

Methods:

- <code title="post /images/edits">client.images.edits.<a href="./src/omnistack/resources/images/edits.py">create</a>(\*\*<a href="src/omnistack/types/images/edit_create_params.py">params</a>) -> <a href="./src/omnistack/types/image_response.py">ImageResponse</a></code>

## Variations

Methods:

- <code title="post /images/variations">client.images.variations.<a href="./src/omnistack/resources/images/variations.py">create</a>(\*\*<a href="src/omnistack/types/images/variation_create_params.py">params</a>) -> <a href="./src/omnistack/types/image_response.py">ImageResponse</a></code>

# Embeddings

Types:

```python
from omnistack.types import EmbeddingCreateResponse
```

Methods:

- <code title="post /embeddings">client.embeddings.<a href="./src/omnistack/resources/embeddings.py">create</a>(\*\*<a href="src/omnistack/types/embedding_create_params.py">params</a>) -> <a href="./src/omnistack/types/embedding_create_response.py">EmbeddingCreateResponse</a></code>

# Audio

## Speech

Methods:

- <code title="post /audio/speech">client.audio.speech.<a href="./src/omnistack/resources/audio/speech.py">create</a>(\*\*<a href="src/omnistack/types/audio/speech_create_params.py">params</a>) -> BinaryAPIResponse</code>

## Transcriptions

Types:

```python
from omnistack.types.audio import TranscriptionCreateResponse
```

Methods:

- <code title="post /audio/transcriptions">client.audio.transcriptions.<a href="./src/omnistack/resources/audio/transcriptions.py">create</a>(\*\*<a href="src/omnistack/types/audio/transcription_create_params.py">params</a>) -> <a href="./src/omnistack/types/audio/transcription_create_response.py">TranscriptionCreateResponse</a></code>

## Translations

Types:

```python
from omnistack.types.audio import TranslationCreateResponse
```

Methods:

- <code title="post /audio/translations">client.audio.translations.<a href="./src/omnistack/resources/audio/translations.py">create</a>(\*\*<a href="src/omnistack/types/audio/translation_create_params.py">params</a>) -> <a href="./src/omnistack/types/audio/translation_create_response.py">TranslationCreateResponse</a></code>

# Files

Types:

```python
from omnistack.types import OpenAIFile, FileListResponse, FileDeleteResponse
```

Methods:

- <code title="post /files">client.files.<a href="./src/omnistack/resources/files/files.py">create</a>(\*\*<a href="src/omnistack/types/file_create_params.py">params</a>) -> <a href="./src/omnistack/types/openai_file.py">OpenAIFile</a></code>
- <code title="get /files/{file_id}">client.files.<a href="./src/omnistack/resources/files/files.py">retrieve</a>(file_id) -> <a href="./src/omnistack/types/openai_file.py">OpenAIFile</a></code>
- <code title="get /files">client.files.<a href="./src/omnistack/resources/files/files.py">list</a>(\*\*<a href="src/omnistack/types/file_list_params.py">params</a>) -> <a href="./src/omnistack/types/file_list_response.py">FileListResponse</a></code>
- <code title="delete /files/{file_id}">client.files.<a href="./src/omnistack/resources/files/files.py">delete</a>(file_id) -> <a href="./src/omnistack/types/file_delete_response.py">FileDeleteResponse</a></code>

## Content

Types:

```python
from omnistack.types.files import ContentRetrieveResponse
```

Methods:

- <code title="get /files/{file_id}/content">client.files.content.<a href="./src/omnistack/resources/files/content.py">retrieve</a>(file_id) -> str</code>

# Uploads

Types:

```python
from omnistack.types import Upload, UploadPart
```

Methods:

- <code title="post /uploads">client.uploads.<a href="./src/omnistack/resources/uploads/uploads.py">create</a>(\*\*<a href="src/omnistack/types/upload_create_params.py">params</a>) -> <a href="./src/omnistack/types/upload.py">Upload</a></code>
- <code title="post /uploads/{upload_id}/cancel">client.uploads.<a href="./src/omnistack/resources/uploads/uploads.py">cancel</a>(upload_id) -> <a href="./src/omnistack/types/upload.py">Upload</a></code>
- <code title="post /uploads/{upload_id}/complete">client.uploads.<a href="./src/omnistack/resources/uploads/uploads.py">complete</a>(upload_id, \*\*<a href="src/omnistack/types/upload_complete_params.py">params</a>) -> <a href="./src/omnistack/types/upload.py">Upload</a></code>

## Parts

Methods:

- <code title="post /uploads/{upload_id}/parts">client.uploads.parts.<a href="./src/omnistack/resources/uploads/parts.py">create</a>(upload_id, \*\*<a href="src/omnistack/types/uploads/part_create_params.py">params</a>) -> <a href="./src/omnistack/types/upload_part.py">UploadPart</a></code>

# FineTuning

## Jobs

Types:

```python
from omnistack.types.fine_tuning import FineTuningJob, JobListResponse
```

Methods:

- <code title="post /fine_tuning/jobs">client.fine_tuning.jobs.<a href="./src/omnistack/resources/fine_tuning/jobs/jobs.py">create</a>(\*\*<a href="src/omnistack/types/fine_tuning/job_create_params.py">params</a>) -> <a href="./src/omnistack/types/fine_tuning/fine_tuning_job.py">FineTuningJob</a></code>
- <code title="get /fine_tuning/jobs/{fine_tuning_job_id}">client.fine_tuning.jobs.<a href="./src/omnistack/resources/fine_tuning/jobs/jobs.py">retrieve</a>(fine_tuning_job_id) -> <a href="./src/omnistack/types/fine_tuning/fine_tuning_job.py">FineTuningJob</a></code>
- <code title="get /fine_tuning/jobs">client.fine_tuning.jobs.<a href="./src/omnistack/resources/fine_tuning/jobs/jobs.py">list</a>(\*\*<a href="src/omnistack/types/fine_tuning/job_list_params.py">params</a>) -> <a href="./src/omnistack/types/fine_tuning/job_list_response.py">JobListResponse</a></code>
- <code title="post /fine_tuning/jobs/{fine_tuning_job_id}/cancel">client.fine_tuning.jobs.<a href="./src/omnistack/resources/fine_tuning/jobs/jobs.py">cancel</a>(fine_tuning_job_id) -> <a href="./src/omnistack/types/fine_tuning/fine_tuning_job.py">FineTuningJob</a></code>

### Events

Types:

```python
from omnistack.types.fine_tuning.jobs import EventRetrieveResponse
```

Methods:

- <code title="get /fine_tuning/jobs/{fine_tuning_job_id}/events">client.fine_tuning.jobs.events.<a href="./src/omnistack/resources/fine_tuning/jobs/events.py">retrieve</a>(fine_tuning_job_id, \*\*<a href="src/omnistack/types/fine_tuning/jobs/event_retrieve_params.py">params</a>) -> <a href="./src/omnistack/types/fine_tuning/jobs/event_retrieve_response.py">EventRetrieveResponse</a></code>

### Checkpoints

Types:

```python
from omnistack.types.fine_tuning.jobs import CheckpointListResponse
```

Methods:

- <code title="get /fine_tuning/jobs/{fine_tuning_job_id}/checkpoints">client.fine_tuning.jobs.checkpoints.<a href="./src/omnistack/resources/fine_tuning/jobs/checkpoints.py">list</a>(fine_tuning_job_id, \*\*<a href="src/omnistack/types/fine_tuning/jobs/checkpoint_list_params.py">params</a>) -> <a href="./src/omnistack/types/fine_tuning/jobs/checkpoint_list_response.py">CheckpointListResponse</a></code>

# Models

Types:

```python
from omnistack.types import Model, ModelListResponse, ModelDeleteResponse
```

Methods:

- <code title="get /models/{model}">client.models.<a href="./src/omnistack/resources/models.py">retrieve</a>(model) -> <a href="./src/omnistack/types/model.py">Model</a></code>
- <code title="get /models">client.models.<a href="./src/omnistack/resources/models.py">list</a>() -> <a href="./src/omnistack/types/model_list_response.py">ModelListResponse</a></code>
- <code title="delete /models/{model}">client.models.<a href="./src/omnistack/resources/models.py">delete</a>(model) -> <a href="./src/omnistack/types/model_delete_response.py">ModelDeleteResponse</a></code>

# Moderations

Types:

```python
from omnistack.types import ModerationCreateResponse
```

Methods:

- <code title="post /moderations">client.moderations.<a href="./src/omnistack/resources/moderations.py">create</a>(\*\*<a href="src/omnistack/types/moderation_create_params.py">params</a>) -> <a href="./src/omnistack/types/moderation_create_response.py">ModerationCreateResponse</a></code>

# Assistants

Types:

```python
from omnistack.types import AssistantObject, AssistantListResponse, AssistantDeleteResponse
```

Methods:

- <code title="post /assistants/{assistant_id}">client.assistants.<a href="./src/omnistack/resources/assistants/assistants.py">create</a>(assistant_id, \*\*<a href="src/omnistack/types/assistant_create_params.py">params</a>) -> <a href="./src/omnistack/types/assistant_object.py">AssistantObject</a></code>
- <code title="get /assistants/{assistant_id}">client.assistants.<a href="./src/omnistack/resources/assistants/assistants.py">retrieve</a>(assistant_id) -> <a href="./src/omnistack/types/assistant_object.py">AssistantObject</a></code>
- <code title="get /assistants">client.assistants.<a href="./src/omnistack/resources/assistants/assistants.py">list</a>(\*\*<a href="src/omnistack/types/assistant_list_params.py">params</a>) -> <a href="./src/omnistack/types/assistant_list_response.py">AssistantListResponse</a></code>
- <code title="delete /assistants/{assistant_id}">client.assistants.<a href="./src/omnistack/resources/assistants/assistants.py">delete</a>(assistant_id) -> <a href="./src/omnistack/types/assistant_delete_response.py">AssistantDeleteResponse</a></code>

## Threads

Types:

```python
from omnistack.types.assistants import MessageObject, RunObject, ThreadObject
```

# Threads

Types:

```python
from omnistack.types import ThreadDeleteResponse
```

Methods:

- <code title="post /threads">client.threads.<a href="./src/omnistack/resources/threads/threads.py">create</a>(\*\*<a href="src/omnistack/types/thread_create_params.py">params</a>) -> <a href="./src/omnistack/types/assistants/thread_object.py">ThreadObject</a></code>
- <code title="get /threads/{thread_id}">client.threads.<a href="./src/omnistack/resources/threads/threads.py">retrieve</a>(thread_id) -> <a href="./src/omnistack/types/assistants/thread_object.py">ThreadObject</a></code>
- <code title="post /threads/{thread_id}">client.threads.<a href="./src/omnistack/resources/threads/threads.py">update</a>(thread_id, \*\*<a href="src/omnistack/types/thread_update_params.py">params</a>) -> <a href="./src/omnistack/types/assistants/thread_object.py">ThreadObject</a></code>
- <code title="delete /threads/{thread_id}">client.threads.<a href="./src/omnistack/resources/threads/threads.py">delete</a>(thread_id) -> <a href="./src/omnistack/types/thread_delete_response.py">ThreadDeleteResponse</a></code>

## Messages

Types:

```python
from omnistack.types.threads import MessageListResponse, MessageDeleteResponse
```

Methods:

- <code title="post /threads/{thread_id}/messages/{message_id}">client.threads.messages.<a href="./src/omnistack/resources/threads/messages.py">create</a>(message_id, \*, thread_id, \*\*<a href="src/omnistack/types/threads/message_create_params.py">params</a>) -> <a href="./src/omnistack/types/assistants/message_object.py">MessageObject</a></code>
- <code title="get /threads/{thread_id}/messages/{message_id}">client.threads.messages.<a href="./src/omnistack/resources/threads/messages.py">retrieve</a>(message_id, \*, thread_id) -> <a href="./src/omnistack/types/assistants/message_object.py">MessageObject</a></code>
- <code title="get /threads/{thread_id}/messages">client.threads.messages.<a href="./src/omnistack/resources/threads/messages.py">list</a>(thread_id, \*\*<a href="src/omnistack/types/threads/message_list_params.py">params</a>) -> <a href="./src/omnistack/types/threads/message_list_response.py">MessageListResponse</a></code>
- <code title="delete /threads/{thread_id}/messages/{message_id}">client.threads.messages.<a href="./src/omnistack/resources/threads/messages.py">delete</a>(message_id, \*, thread_id) -> <a href="./src/omnistack/types/threads/message_delete_response.py">MessageDeleteResponse</a></code>

## Runs

Types:

```python
from omnistack.types.threads import RunListResponse
```

Methods:

- <code title="post /threads/{thread_id}/runs/{run_id}">client.threads.runs.<a href="./src/omnistack/resources/threads/runs/runs.py">create</a>(run_id, \*, thread_id, \*\*<a href="src/omnistack/types/threads/run_create_params.py">params</a>) -> <a href="./src/omnistack/types/assistants/run_object.py">RunObject</a></code>
- <code title="get /threads/{thread_id}/runs/{run_id}">client.threads.runs.<a href="./src/omnistack/resources/threads/runs/runs.py">retrieve</a>(run_id, \*, thread_id) -> <a href="./src/omnistack/types/assistants/run_object.py">RunObject</a></code>
- <code title="get /threads/{thread_id}/runs">client.threads.runs.<a href="./src/omnistack/resources/threads/runs/runs.py">list</a>(thread_id, \*\*<a href="src/omnistack/types/threads/run_list_params.py">params</a>) -> <a href="./src/omnistack/types/threads/run_list_response.py">RunListResponse</a></code>
- <code title="post /threads/{thread_id}/runs/{run_id}/cancel">client.threads.runs.<a href="./src/omnistack/resources/threads/runs/runs.py">cancel</a>(run_id, \*, thread_id) -> <a href="./src/omnistack/types/assistants/run_object.py">RunObject</a></code>
- <code title="post /threads/{thread_id}/runs/{run_id}/submit_tool_outputs">client.threads.runs.<a href="./src/omnistack/resources/threads/runs/runs.py">submit_tool_outputs</a>(run_id, \*, thread_id, \*\*<a href="src/omnistack/types/threads/run_submit_tool_outputs_params.py">params</a>) -> <a href="./src/omnistack/types/assistants/run_object.py">RunObject</a></code>

### Steps

Types:

```python
from omnistack.types.threads.runs import RunStepObject, StepListResponse
```

Methods:

- <code title="get /threads/{thread_id}/runs/{run_id}/steps/{step_id}">client.threads.runs.steps.<a href="./src/omnistack/resources/threads/runs/steps.py">retrieve</a>(step_id, \*, thread_id, run_id, \*\*<a href="src/omnistack/types/threads/runs/step_retrieve_params.py">params</a>) -> <a href="./src/omnistack/types/threads/runs/run_step_object.py">RunStepObject</a></code>
- <code title="get /threads/{thread_id}/runs/{run_id}/steps">client.threads.runs.steps.<a href="./src/omnistack/resources/threads/runs/steps.py">list</a>(run_id, \*, thread_id, \*\*<a href="src/omnistack/types/threads/runs/step_list_params.py">params</a>) -> <a href="./src/omnistack/types/threads/runs/step_list_response.py">StepListResponse</a></code>

# VectorStores

Types:

```python
from omnistack.types import VectorStoreObject, VectorStoreListResponse, VectorStoreDeleteResponse
```

Methods:

- <code title="post /vector_stores">client.vector_stores.<a href="./src/omnistack/resources/vector_stores/vector_stores.py">create</a>(\*\*<a href="src/omnistack/types/vector_store_create_params.py">params</a>) -> <a href="./src/omnistack/types/vector_store_object.py">VectorStoreObject</a></code>
- <code title="get /vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/omnistack/resources/vector_stores/vector_stores.py">retrieve</a>(vector_store_id) -> <a href="./src/omnistack/types/vector_store_object.py">VectorStoreObject</a></code>
- <code title="post /vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/omnistack/resources/vector_stores/vector_stores.py">update</a>(vector_store_id, \*\*<a href="src/omnistack/types/vector_store_update_params.py">params</a>) -> <a href="./src/omnistack/types/vector_store_object.py">VectorStoreObject</a></code>
- <code title="get /vector_stores">client.vector_stores.<a href="./src/omnistack/resources/vector_stores/vector_stores.py">list</a>(\*\*<a href="src/omnistack/types/vector_store_list_params.py">params</a>) -> <a href="./src/omnistack/types/vector_store_list_response.py">VectorStoreListResponse</a></code>
- <code title="delete /vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/omnistack/resources/vector_stores/vector_stores.py">delete</a>(vector_store_id) -> <a href="./src/omnistack/types/vector_store_delete_response.py">VectorStoreDeleteResponse</a></code>

## Files

Types:

```python
from omnistack.types.vector_stores import (
    VectorStoreFileObject,
    FileListResponse,
    FileDeleteResponse,
)
```

Methods:

- <code title="post /vector_stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/omnistack/resources/vector_stores/files.py">create</a>(vector_store_id, \*\*<a href="src/omnistack/types/vector_stores/file_create_params.py">params</a>) -> <a href="./src/omnistack/types/vector_stores/vector_store_file_object.py">VectorStoreFileObject</a></code>
- <code title="get /vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/omnistack/resources/vector_stores/files.py">retrieve</a>(file_id, \*, vector_store_id) -> <a href="./src/omnistack/types/vector_stores/vector_store_file_object.py">VectorStoreFileObject</a></code>
- <code title="get /vector_stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/omnistack/resources/vector_stores/files.py">list</a>(vector_store_id, \*\*<a href="src/omnistack/types/vector_stores/file_list_params.py">params</a>) -> <a href="./src/omnistack/types/vector_stores/file_list_response.py">FileListResponse</a></code>
- <code title="delete /vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/omnistack/resources/vector_stores/files.py">delete</a>(file_id, \*, vector_store_id) -> <a href="./src/omnistack/types/vector_stores/file_delete_response.py">FileDeleteResponse</a></code>

## FileBatches

Types:

```python
from omnistack.types.vector_stores import VectorStoreFileBatchObject
```

Methods:

- <code title="post /vector_stores/{vector_store_id}/file_batches">client.vector_stores.file_batches.<a href="./src/omnistack/resources/vector_stores/file_batches/file_batches.py">create</a>(vector_store_id, \*\*<a href="src/omnistack/types/vector_stores/file_batch_create_params.py">params</a>) -> <a href="./src/omnistack/types/vector_stores/vector_store_file_batch_object.py">VectorStoreFileBatchObject</a></code>
- <code title="get /vector_stores/{vector_store_id}/file_batches/{batch_id}">client.vector_stores.file_batches.<a href="./src/omnistack/resources/vector_stores/file_batches/file_batches.py">retrieve</a>(batch_id, \*, vector_store_id) -> <a href="./src/omnistack/types/vector_stores/vector_store_file_batch_object.py">VectorStoreFileBatchObject</a></code>
- <code title="post /vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel">client.vector_stores.file_batches.<a href="./src/omnistack/resources/vector_stores/file_batches/file_batches.py">cancel</a>(batch_id, \*, vector_store_id) -> <a href="./src/omnistack/types/vector_stores/vector_store_file_batch_object.py">VectorStoreFileBatchObject</a></code>

### Files

Types:

```python
from omnistack.types.vector_stores.file_batches import FileListResponse
```

Methods:

- <code title="get /vector_stores/{vector_store_id}/file_batches/{batch_id}/files">client.vector_stores.file_batches.files.<a href="./src/omnistack/resources/vector_stores/file_batches/files.py">list</a>(batch_id, \*, vector_store_id, \*\*<a href="src/omnistack/types/vector_stores/file_batches/file_list_params.py">params</a>) -> <a href="./src/omnistack/types/vector_stores/file_batches/file_list_response.py">FileListResponse</a></code>

# Batches

Types:

```python
from omnistack.types import Batch, BatchListResponse
```

Methods:

- <code title="post /batches">client.batches.<a href="./src/omnistack/resources/batches.py">create</a>(\*\*<a href="src/omnistack/types/batch_create_params.py">params</a>) -> <a href="./src/omnistack/types/batch.py">Batch</a></code>
- <code title="get /batches/{batch_id}">client.batches.<a href="./src/omnistack/resources/batches.py">retrieve</a>(batch_id) -> <a href="./src/omnistack/types/batch.py">Batch</a></code>
- <code title="get /batches">client.batches.<a href="./src/omnistack/resources/batches.py">list</a>(\*\*<a href="src/omnistack/types/batch_list_params.py">params</a>) -> <a href="./src/omnistack/types/batch_list_response.py">BatchListResponse</a></code>
- <code title="post /batches/{batch_id}/cancel">client.batches.<a href="./src/omnistack/resources/batches.py">cancel</a>(batch_id) -> <a href="./src/omnistack/types/batch.py">Batch</a></code>

# Organization

## AuditLogs

Types:

```python
from omnistack.types.organization import AuditLogListResponse
```

Methods:

- <code title="get /organization/audit_logs">client.organization.audit_logs.<a href="./src/omnistack/resources/organization/audit_logs.py">list</a>(\*\*<a href="src/omnistack/types/organization/audit_log_list_params.py">params</a>) -> <a href="./src/omnistack/types/organization/audit_log_list_response.py">AuditLogListResponse</a></code>

## Invites

Types:

```python
from omnistack.types.organization import Invite, InviteListResponse, InviteDeleteResponse
```

Methods:

- <code title="post /organization/invites">client.organization.invites.<a href="./src/omnistack/resources/organization/invites.py">create</a>(\*\*<a href="src/omnistack/types/organization/invite_create_params.py">params</a>) -> <a href="./src/omnistack/types/organization/invite.py">Invite</a></code>
- <code title="get /organization/invites/{invite_id}">client.organization.invites.<a href="./src/omnistack/resources/organization/invites.py">retrieve</a>(invite_id) -> <a href="./src/omnistack/types/organization/invite.py">Invite</a></code>
- <code title="get /organization/invites">client.organization.invites.<a href="./src/omnistack/resources/organization/invites.py">list</a>(\*\*<a href="src/omnistack/types/organization/invite_list_params.py">params</a>) -> <a href="./src/omnistack/types/organization/invite_list_response.py">InviteListResponse</a></code>
- <code title="delete /organization/invites/{invite_id}">client.organization.invites.<a href="./src/omnistack/resources/organization/invites.py">delete</a>(invite_id) -> <a href="./src/omnistack/types/organization/invite_delete_response.py">InviteDeleteResponse</a></code>

## Users

Types:

```python
from omnistack.types.organization import User, UserListResponse, UserDeleteResponse
```

Methods:

- <code title="post /organization/users/{user_id}">client.organization.users.<a href="./src/omnistack/resources/organization/users.py">create</a>(user_id, \*\*<a href="src/omnistack/types/organization/user_create_params.py">params</a>) -> <a href="./src/omnistack/types/organization/user.py">User</a></code>
- <code title="get /organization/users/{user_id}">client.organization.users.<a href="./src/omnistack/resources/organization/users.py">retrieve</a>(user_id) -> <a href="./src/omnistack/types/organization/user.py">User</a></code>
- <code title="get /organization/users">client.organization.users.<a href="./src/omnistack/resources/organization/users.py">list</a>(\*\*<a href="src/omnistack/types/organization/user_list_params.py">params</a>) -> <a href="./src/omnistack/types/organization/user_list_response.py">UserListResponse</a></code>
- <code title="delete /organization/users/{user_id}">client.organization.users.<a href="./src/omnistack/resources/organization/users.py">delete</a>(user_id) -> <a href="./src/omnistack/types/organization/user_delete_response.py">UserDeleteResponse</a></code>

## Projects

Types:

```python
from omnistack.types.organization import Project, ProjectListResponse
```

Methods:

- <code title="post /organization/projects/{project_id}">client.organization.projects.<a href="./src/omnistack/resources/organization/projects/projects.py">create</a>(project_id, \*\*<a href="src/omnistack/types/organization/project_create_params.py">params</a>) -> <a href="./src/omnistack/types/organization/project.py">Project</a></code>
- <code title="get /organization/projects/{project_id}">client.organization.projects.<a href="./src/omnistack/resources/organization/projects/projects.py">retrieve</a>(project_id) -> <a href="./src/omnistack/types/organization/project.py">Project</a></code>
- <code title="get /organization/projects">client.organization.projects.<a href="./src/omnistack/resources/organization/projects/projects.py">list</a>(\*\*<a href="src/omnistack/types/organization/project_list_params.py">params</a>) -> <a href="./src/omnistack/types/organization/project_list_response.py">ProjectListResponse</a></code>
- <code title="post /organization/projects/{project_id}/archive">client.organization.projects.<a href="./src/omnistack/resources/organization/projects/projects.py">archive</a>(project_id) -> <a href="./src/omnistack/types/organization/project.py">Project</a></code>

### Users

Types:

```python
from omnistack.types.organization.projects import UserListResponse, UserDeleteResponse
```

Methods:

- <code title="post /organization/projects/{project_id}/users/{user_id}">client.organization.projects.users.<a href="./src/omnistack/resources/organization/projects/users.py">create</a>(user_id, \*, project_id, \*\*<a href="src/omnistack/types/organization/projects/user_create_params.py">params</a>) -> <a href="./src/omnistack/types/shared/project_user.py">ProjectUser</a></code>
- <code title="get /organization/projects/{project_id}/users/{user_id}">client.organization.projects.users.<a href="./src/omnistack/resources/organization/projects/users.py">retrieve</a>(user_id, \*, project_id) -> <a href="./src/omnistack/types/shared/project_user.py">ProjectUser</a></code>
- <code title="get /organization/projects/{project_id}/users">client.organization.projects.users.<a href="./src/omnistack/resources/organization/projects/users.py">list</a>(project_id, \*\*<a href="src/omnistack/types/organization/projects/user_list_params.py">params</a>) -> <a href="./src/omnistack/types/organization/projects/user_list_response.py">UserListResponse</a></code>
- <code title="delete /organization/projects/{project_id}/users/{user_id}">client.organization.projects.users.<a href="./src/omnistack/resources/organization/projects/users.py">delete</a>(user_id, \*, project_id) -> <a href="./src/omnistack/types/organization/projects/user_delete_response.py">UserDeleteResponse</a></code>

### ServiceAccounts

Types:

```python
from omnistack.types.organization.projects import (
    ServiceAccountCreateResponse,
    ServiceAccountListResponse,
)
```

Methods:

- <code title="post /organization/projects/{project_id}/service_accounts">client.organization.projects.service_accounts.<a href="./src/omnistack/resources/organization/projects/service_accounts.py">create</a>(project_id, \*\*<a href="src/omnistack/types/organization/projects/service_account_create_params.py">params</a>) -> <a href="./src/omnistack/types/organization/projects/service_account_create_response.py">ServiceAccountCreateResponse</a></code>
- <code title="get /organization/projects/{project_id}/service_accounts/{service_account_id}">client.organization.projects.service_accounts.<a href="./src/omnistack/resources/organization/projects/service_accounts.py">retrieve</a>(service_account_id, \*, project_id) -> <a href="./src/omnistack/types/shared/project_service_account.py">ProjectServiceAccount</a></code>
- <code title="get /organization/projects/{project_id}/service_accounts">client.organization.projects.service_accounts.<a href="./src/omnistack/resources/organization/projects/service_accounts.py">list</a>(project_id, \*\*<a href="src/omnistack/types/organization/projects/service_account_list_params.py">params</a>) -> <a href="./src/omnistack/types/organization/projects/service_account_list_response.py">ServiceAccountListResponse</a></code>

# Projects

## ServiceAccounts

Types:

```python
from omnistack.types.projects import ServiceAccountDeleteResponse
```

Methods:

- <code title="delete /organization/projects/{project_id}/service_accounts/{service_account_id}">client.projects.service_accounts.<a href="./src/omnistack/resources/projects/service_accounts.py">delete</a>(service_account_id, \*, project_id) -> <a href="./src/omnistack/types/projects/service_account_delete_response.py">ServiceAccountDeleteResponse</a></code>

## APIKeys

Types:

```python
from omnistack.types.projects import APIKeyListResponse, APIKeyDeleteResponse
```

Methods:

- <code title="get /organization/projects/{project_id}/api_keys/{key_id}">client.projects.api_keys.<a href="./src/omnistack/resources/projects/api_keys.py">retrieve</a>(key_id, \*, project_id) -> <a href="./src/omnistack/types/shared/project_api_key.py">ProjectAPIKey</a></code>
- <code title="get /organization/projects/{project_id}/api_keys">client.projects.api_keys.<a href="./src/omnistack/resources/projects/api_keys.py">list</a>(project_id, \*\*<a href="src/omnistack/types/projects/api_key_list_params.py">params</a>) -> <a href="./src/omnistack/types/projects/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /organization/projects/{project_id}/api_keys/{key_id}">client.projects.api_keys.<a href="./src/omnistack/resources/projects/api_keys.py">delete</a>(key_id, \*, project_id) -> <a href="./src/omnistack/types/projects/api_key_delete_response.py">APIKeyDeleteResponse</a></code>
