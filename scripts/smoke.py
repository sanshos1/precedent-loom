import json,re,time
from pathlib import Path
from genlayer_py import create_account,create_client
from genlayer_py.chains import studionet
from genlayer_py.types import TransactionStatus
R=Path(__file__).parents[1];env=(R.parents[3]/'accounts.env').read_text();address=json.loads((R/'deployment.json').read_text())['contractAddress']
def client(n):
 key=re.search(rf'^ACCOUNT_{n}_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)',env,re.M).group(1).strip();return create_client(chain=studionet,account=create_account(account_private_key=key))
def write(n,name,args):
 c=client(n);tx=c.write_contract(address=address,function_name=name,args=args);print(name+'_tx='+str(tx),flush=True);r=c.wait_for_transaction_receipt(transaction_hash=tx,status=TransactionStatus.FINALIZED,retries=180,interval=5000,full_transaction=True);leader=(r.get('consensus_data',{}).get('leader_receipt')or[{}])[0];assert r.get('result_name')=='MAJORITY_AGREE' and leader.get('execution_result')=='SUCCESS';return str(tx)
stamp=str(int(time.time()));book='ACCESS-'+stamp;case='EAST-'+stamp;policy='https://raw.githubusercontent.com/sanshos1/precedent-loom/main/evidence/policy.md';request='https://cdn.jsdelivr.net/gh/sanshos1/precedent-loom@main/evidence/case-one.md';txs={'open':write(3,'open_book',[book,'Accessibility route exceptions',policy,['Grant only for a documented access barrier with an equivalent safe alternative','Deny convenience-only requests without an access barrier','Mark requests insufficient when barrier or safe alternative is missing']]),'file':write(1,'file_case',[book,case,request]),'evaluate':write(2,'evaluate',[book,case])};state=client(3).read_contract(address=address,function_name='get_case',args=[book,case]);assert state['state']=='FINAL' and state['decision']=='GRANT' and state['rule_indexes'];proof={'bookId':book,'caseId':case,'transactions':txs,'state':state,'walletDisclosure':'All wallets are operator-controlled demo wallets.'};(R/'evidence'/'live-proof.json').write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof,indent=2),flush=True)

